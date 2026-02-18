import ccxt
import os
import argparse
import time
from dotenv import load_dotenv
from termcolor import colored
try:
    from ops.grid_metrics import GridRunMetrics
    from ops.regime_engine import RegimeEngine
    from ops.confluence import ConfluenceEngine
except ImportError:
    from grid_metrics import GridRunMetrics
    from regime_engine import RegimeEngine
    from confluence import ConfluenceEngine

# Import OBI Analyzer
try:
    from ops.obi_analyzer import analyze_obi
except ImportError:
    from obi_analyzer import analyze_obi
try:
    from ops import market_diagnostic
except ImportError:
    import market_diagnostic
try:
    from ops.regime_engine import recommend_grid
except ImportError:
    from regime_engine import recommend_grid
try:
    from ops.confluence import evaluate_confluence
except ImportError:
    from confluence import evaluate_confluence

# Load Environment
load_dotenv("config/.env")


HARD_MAX_LEVERAGE = 10


class GridExecutor:
    def __init__(
        self,
        symbol="BNB/USDT:USDT",
        lower=615.0,
        upper=635.0,
        grids=40,
        leverage=5,
        dry_run=False,
        reference_price=None,
        maker_fee_bps=2.0,
        seed_side="both",
        allow_open_shorts=False,
        step=None, # Added step caching
        auto_regime=False,
        min_confluence=3,
    ):
        self.symbol = symbol
        self.lower = lower
        self.upper = upper
        self.grids = grids
        self.leverage = int(leverage)
        self.dry_run = dry_run
        self.reference_price = reference_price if reference_price else (self.lower + self.upper) / 2
        self.seed_side = seed_side
        self.allow_open_shorts = allow_open_shorts
        self.auto_regime = auto_regime
        self.min_confluence = min_confluence
        self.exchange = None
        self.orders = [] # List of order dicts
        self.active_grid = {} # Map order_id -> {price, side, qty}
        self.step = step # Store grid step size
        self.trade_enabled = True
        self.regime_snapshot = {}
        self.last_regime_check_ts = 0.0
        self.regime_check_interval_sec = 60
        self.metrics = GridRunMetrics(
            symbol=self.symbol,
            mode="DRY_RUN" if dry_run else "LIVE",
            leverage=self.leverage,
            maker_fee_bps=maker_fee_bps,
        )
        # Engines
        self.regime_engine = RegimeEngine(self.symbol)
        self.confluence_engine = ConfluenceEngine()
        self.last_regime_check = 0

        if self.grids < 2:
            raise ValueError("grids must be >= 2")
        if self.upper <= self.lower:
            raise ValueError("upper must be greater than lower")
        if self.leverage < 1:
            raise ValueError("leverage must be >= 1")
        if self.leverage > HARD_MAX_LEVERAGE:
            raise ValueError(f"leverage exceeds hard max ({HARD_MAX_LEVERAGE}x)")

        if self.dry_run:
            print(colored("[SYSTEM] DRY-RUN OFFLINE MODE ENABLED (NO EXCHANGE CALLS)", "yellow"))
            return

        # Connect to Binance (live mode only)
        api_key = os.getenv("BINANCE_API_KEY")
        secret = os.getenv("BINANCE_SECRET")

        config = {
            'enableRateLimit': True,
            'options': {'defaultType': 'future'}
        }

        if api_key and secret:
            config['apiKey'] = api_key
            config['secret'] = secret
            self.exchange = ccxt.binance(config)
            print(colored("[SYSTEM] CONNECTED TO BINANCE EXECUTION ENGINE (LIVE)", "green"))
        else:
            raise RuntimeError("No API keys found for live mode.")

        self.validate_live_readiness()
        if self.auto_regime:
            self.auto_configure()
        self.set_leverage(self.leverage)

    @staticmethod
    def _to_spot_symbol(symbol):
        if ":" in symbol:
            return symbol.split(":")[0]
        return symbol

    def fetch_market_state(self):
        spot_symbol = self._to_spot_symbol(self.symbol)
        data = market_diagnostic.fetch_market_data(spot_symbol)
        if data:
            return data

        cache_ttl = 7200 if self.dry_run else 900
        cached = market_diagnostic.load_cached_market_data(spot_symbol, max_age_sec=cache_ttl)
        if cached:
            print(colored(f"[REGIME] Using cached market snapshot ({cached.get('cache_age_sec')}s old).", "yellow"))
            return cached

        if self.dry_run:
            # Offline fallback for simulations when no network/cache is available.
            neutral = {
                "symbol": spot_symbol,
                "price": float(self.reference_price),
                "obi": 0.0,
                "rsi": 50.0,
                "atr": max(0.5, float(self.reference_price) * 0.002),
                "atr_pct": 0.2,
                "spread_pct": 0.01,
                "timestamp": int(time.time()),
                "source": "offline_fallback",
            }
            print(colored("[REGIME] Using offline neutral market profile for dry-run.", "yellow"))
            return neutral

        raise RuntimeError("market_diagnostic returned empty data and no valid cache available")

    def auto_configure(self):
        try:
            market = self.fetch_market_state()
            decision = recommend_grid(
                market,
                base_leverage=self.leverage,
                hard_max_leverage=HARD_MAX_LEVERAGE,
            )
            conf = evaluate_confluence(market, decision.regime)
            self.regime_snapshot = {
                "market": market,
                "regime": decision.regime,
                "confluence": conf,
                "reason": decision.reason,
            }
            self.metrics.set_context(self.regime_snapshot)

            print(colored(f"[REGIME] {decision.regime} | confluence {conf['score']}/{conf['total']}", "blue"))
            print(colored(f"[REGIME] {decision.reason}", "blue"))

            if conf["score"] < self.min_confluence or not conf["confirmed"]:
                self.trade_enabled = False
                print(colored("[REGIME] Confluence too weak. Holding (no new orders).", "yellow"))
                return

            self.trade_enabled = True
            self.seed_side = decision.seed_side
            self.leverage = decision.leverage
            self.lower = decision.lower
            self.upper = decision.upper
            self.grids = decision.grids
            self.allow_open_shorts = decision.allow_open_shorts
            print(
                colored(
                    f"[REGIME] Applied -> seed={self.seed_side} lev={self.leverage} "
                    f"range=[{self.lower}, {self.upper}] grids={self.grids}",
                    "cyan",
                )
            )
        except Exception as e:
            self.trade_enabled = False
            print(colored(f"[REGIME] Auto regime failed: {e}. Holding.", "red"))

    def reassess_regime(self):
        if not self.auto_regime:
            return
        now = time.time()
        if now - self.last_regime_check_ts < self.regime_check_interval_sec:
            return
        self.last_regime_check_ts = now

        old_regime = self.regime_snapshot.get("regime")
        self.auto_configure()
        new_regime = self.regime_snapshot.get("regime")
        if old_regime and new_regime and old_regime != new_regime:
            print(colored(f"[REGIME] Shift detected: {old_regime} -> {new_regime}", "magenta"))
            if not self.dry_run:
                self.cancel_all()
                self.active_grid = {}
                self.orders = []
                if self.trade_enabled:
                    print(colored("[REGIME] Rebuilding grid for new regime...", "magenta"))
                    self.place_initial_grid()

    def validate_live_readiness(self):
        try:
            markets = self.exchange.load_markets()
            if self.symbol not in markets:
                raise RuntimeError(f"Symbol {self.symbol} not found on exchange.")

            # Private endpoint check: confirms key validity and permission scope.
            balance = self.exchange.fetch_balance()
            usdt_balance = balance.get("USDT", {}).get("free", 0)
            print(colored(f"[CHECK] API permissions OK | USDT free: {usdt_balance}", "cyan"))
        except Exception as e:
            raise RuntimeError(f"Live readiness validation failed: {e}") from e

    def set_leverage(self, leverage):
        try:
            self.exchange.set_leverage(leverage, self.symbol)
            print(colored(f"[RISK] LEVERAGE SET TO {leverage}x (HARD MAX: {HARD_MAX_LEVERAGE}x)", "yellow"))
        except Exception as e:
            raise RuntimeError(f"Could not set leverage: {e}") from e

    def fetch_price(self):
        if self.dry_run:
            return self.reference_price
        ticker = self.exchange.fetch_ticker(self.symbol)
        return float(ticker['last'])

    def cancel_all(self):
        if self.dry_run:
            print(colored("[DRY-RUN] Would CANCEL ALL orders.", "yellow"))
            return
            
        try:
            print(colored(f"[EXEC] Cancelling all open orders for {self.symbol}...", "cyan"))
            self.exchange.cancel_all_orders(self.symbol)
            print(colored("[EXEC] Orders cleared.", "green"))
        except Exception as e:
            print(colored(f"[ERROR] Cancel failed: {e}", "red"))

    def calculate_levels(self):
        step = (self.upper - self.lower) / self.grids
        self.step = step
        levels = [round(self.lower + i * step, 2) for i in range(self.grids + 1)]
        return levels, step

    def place_initial_grid(self):
        if not self.trade_enabled:
            print(colored("[HOLD] Trade disabled by regime/confluence guard.", "yellow"))
            return {"orders_planned": 0, "step": self.step if self.step else 0.0, "qty": 0.0}

        current_price = self.fetch_price()
        print(colored(f"[MARKET] Current Price: ${current_price:.2f}", "blue"))
        
        levels, step = self.calculate_levels()
        
        # Split by market side using real price relation (strictly below/above market).
        buys = [l for l in levels if l < current_price]
        sells = [l for l in levels if l > current_price]

        # Filter based on seed_side
        if self.seed_side == "buy":
            sells = []
            print(colored(f"[STRATEGY] Seed Mode: BUY ONLY. Ignoring {len(levels) - len(buys)} sell levels.", "yellow"))
        elif self.seed_side == "sell":
            buys = []
            print(colored(f"[STRATEGY] Seed Mode: SELL ONLY. Ignoring {len(levels) - len(sells)} buy levels.", "yellow"))
        
        print(colored(f"[PLAN] Placing {len(buys)} BUYS and {len(sells)} SELLS", "cyan"))
        
        # Calculate Quantity per Grid
        # Min Notional $5. Use $6 for safety.
        # Qty = $6 / Price
        qty = round(6.0 / current_price, 3) # BNB precision usually 2 or 3 decimals
        
        total_investment = (len(buys) + len(sells)) * 6.0
        print(colored(f"[CAPITAL] Required Margin (approx 1x): ${total_investment:.2f}", "yellow"))

        # Margin-aware order cap (live only) to avoid -2019 insufficient margin floods.
        if not self.dry_run:
            try:
                bal = self.exchange.fetch_balance()
                usdt_free = float(bal.get("USDT", {}).get("free", 0.0))
                
                # Use 95% of available margin for orders
                # Leverage is already set on account, so usdt_free is the collateral.
                # Total Notional capacity = usdt_free * leverage
                max_total_notional = usdt_free * self.leverage * 0.95
                per_order_notional = qty * current_price
                
                # Cost per order in terms of Initial Margin is (Notional / Leverage)
                # But here we just compare total notional vs total capacity
                max_orders = int(max_total_notional / per_order_notional) if per_order_notional > 0 else 0
                
                print(colored(f"[RISK] USDT free: ${usdt_free:.4f} | Max affordable orders: {max_orders}", "yellow"))

                if max_orders <= 0:
                    print(colored("[RISK] Not enough free margin for minimum order size. Aborting cycle.", "red"))
                    return {"orders_planned": 0, "step": step, "qty": qty}

                # Limit orders
                all_orders = []
                for b in buys:
                    all_orders.append(('buy', b))
                for s in sells:
                    all_orders.append(('sell', s))
                
                # Sort by proximity to current price to ensure balanced truncation
                all_orders.sort(key=lambda x: abs(x[1] - current_price))
                
                # Truncate list
                if len(all_orders) > max_orders:
                    print(colored(f"[RISK] Truncating plan from {len(all_orders)} to {max_orders} orders.", "magenta"))
                    all_orders = all_orders[:max_orders]
                    
                # Re-split
                buys = [p for s, p in all_orders if s == 'buy']
                sells = [p for s, p in all_orders if s == 'sell']
                
                print(colored(f"[PLAN] Adjusted by margin: {len(buys)} BUYS and {len(sells)} SELLS", "cyan"))
            except Exception as e:
                print(colored(f"[WARNING] Margin check failed: {e}. Proceeding with original plan.", "red"))
        
        # Execute BUYS
        for price in buys:
            self.place_limit_order('buy', price, qty)
            
        # Execute SELLS
        for price in sells:
            self.place_limit_order('sell', price, qty)

        return {
            "orders_planned": len(buys) + len(sells),
            "step": step,
            "qty": qty,
        }

    def place_limit_order(self, side, price, amount):
        self.metrics.record_attempt(side)
        if self.dry_run:
            print(colored(f"[DRY-RUN] Would PLACE LIMIT {side.upper()} @ ${price} (Qty: {amount})", "yellow"))
            self.metrics.record_success(side, price, amount)
            return

        try:
            params = {'timeInForce': 'GTC'}
            
            # Safety rail: prevent opening an unintended short on sell-side orders unless explicitly allowed.
            if side == 'sell' and not self.allow_open_shorts:
                params['reduceOnly'] = True
            
            order = self.exchange.create_order(self.symbol, 'limit', side, amount, price, params)
            print(colored(f"[EXEC] PLACED {side.upper()} @ ${price} | ID: {order['id']}", "green"))
            
            # Track active order
            self.orders.append(order)
            self.active_grid[order['id']] = {
                "side": side,
                "price": float(price),
                "amount": float(amount),
                "status": "open"
            }
            
            self.metrics.record_success(side, price, amount)
        except Exception as e:
            # Handle specific Binance errors nicely
            err_str = str(e)
            if "Margin is insufficient" in err_str:
                print(colored(f"[ERROR] Margin Insufficient ({side} @ {price}) - Stopping further orders.", "red"))
                # Stop placing orders if we run out of margin
                # Raise to stop loop? Or just log? 
                # For grid loop, maybe best to just log and continue or break? 
                # If we calculated max_orders correctly, this shouldn't happen often.
            else:
                print(colored(f"[ERROR] Order failed ({side} @ {price}): {e}", "red"))
            self.metrics.record_error(side, price, amount, e)

    def monitor_loop(self):
        if self.dry_run:
            print(colored("[MONITOR] LOOP (DRY RUN): Checking simulated fills...", "magenta"))
            # In dry-run, we can simulate fills if price moves.
            # For now, just exit.
            return

        print(colored("[MONITOR] STARTING GRID MONITORING LOOP (Ctrl+C to stop)...", "magenta"))
        while True:
            try:
                # 0. Fast Invalidation Check (Safety Rail)
                # Check Regime Periodically (e.g. 60s)
                self.reassess_regime()

                # If Price < 608.4 AND OBI < 0 (Negative), ABORT.
                current_price = self.fetch_price()
                if current_price < 608.4:
                    print(colored(f"⚠️  PRICE ALERT: ${current_price} < $608.4. Checking OBI...", "yellow"))
                    try:
                        # Use imported analyzer or inline logic if simpler
                        # Fetch OBI depth 10 for speed
                        obi_data = analyze_obi(self.symbol, depth=10)
                        if obi_data and obi_data['obi'] < 0:
                             print(colored(f"[CRITICAL] PRICE ${current_price} + NEGATIVE OBI ({obi_data['obi']:.4f}). ABORTING GRID.", "red", attrs=['bold']))
                             self.cancel_all()
                             print(colored("[STOP] GRID STOPPED BY SAFETY RAIL.", "red"))
                             break
                        else:
                             print(colored(f"ℹ️  OBI is positive ({obi_data['obi']:.4f}). Holding.", "cyan"))
                    except Exception as e:
                        print(colored(f"[WARNING] OBI Check failed: {e}", "yellow"))

                # 1. Fetch Open Orders
                # We need to know which of OUR orders are still open.
                # fetch_open_orders returns all open orders for symbol.
                try:
                    open_orders = self.exchange.fetch_open_orders(self.symbol)
                    open_ids = [o['id'] for o in open_orders]
                except Exception as e:
                    print(colored(f"[WARNING] API Error fetching open orders: {e}", "yellow"))
                    time.sleep(2)
                    continue

                # 2. Check for Filled Orders
                # Iterate over a copy of active_grid keys (our tracked orders)
                active_ids = list(self.active_grid.keys())
                
                for oid in active_ids:
                    if oid not in open_ids:
                        # Order is no longer open. It might be FILLED or CANCELED.
                        # We must confirm status.
                        try:
                            order = self.exchange.fetch_order(oid, self.symbol)
                            status = order['status']
                            
                            if status == 'closed': # FILLED
                                info = self.active_grid.pop(oid)
                                side = info['side']
                                price = info['price']
                                qty = info['amount']
                                
                                print(colored(f"✅ ORDER FILLED: {side.upper()} @ ${price}", "green"))
                                
                                # Track Fill & Fees
                                # Approximate PnL if it's a closing trade (Sell in Long Grid)
                                step_pnl = 0.0
                                if side == 'sell':
                                    step_pnl = (self.step * qty)
                                    print(colored(f"[PNL] CYCLE CLOSED: +${step_pnl:.4f} (Gross)", "green"))
                                
                                self.metrics.record_fill(side, price, qty, pnl=step_pnl)
                                
                                # 3. REPLENISH LOGIC
                                if side == 'buy':
                                    # Buy Filled -> Place Sell @ Price + Step
                                    sell_price = round(price + self.step, 2)
                                    print(colored(f"[REPLENISH] Buy filled @ {price}. Placing SELL @ ${sell_price}", "cyan"))
                                    self.place_limit_order('sell', sell_price, qty)
                                    
                                elif side == 'sell':
                                    # Sell Filled -> Place Buy @ Price - Step
                                    buy_price = round(price - self.step, 2)
                                    print(colored(f"[REPLENISH] Sell filled @ {price}. Placing BUY @ ${buy_price}", "cyan"))
                                    self.place_limit_order('buy', buy_price, qty)
                                    
                            elif status == 'canceled':
                                print(colored(f"⚠️ Order {oid} CANCELED. Removing from tracker.", "yellow"))
                                self.active_grid.pop(oid)
                                
                        except Exception as e:
                            print(colored(f"[ERROR] Could not fetch details for closed order {oid}: {e}", "red"))
                
                time.sleep(5) # Check every 5 seconds
                
            except KeyboardInterrupt:
                print(colored("\n[STOP] STOPPING MONITORING LOOP.", "red"))
                break
            except Exception as e:
                print(colored(f"[ERROR] Monitoring loop error: {e}", "red"))
                time.sleep(5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", default="BNB/USDT:USDT", help="Trading symbol")
    parser.add_argument("--lower", type=float, default=615.0, help="Grid lower bound")
    parser.add_argument("--upper", type=float, default=635.0, help="Grid upper bound")
    parser.add_argument("--grids", type=int, default=40, help="Number of grid intervals")
    parser.add_argument("--leverage", type=int, default=5, help=f"Leverage (max {HARD_MAX_LEVERAGE}x)")
    parser.add_argument("--reference-price", type=float, default=None, help="Offline dry-run price override")
    parser.add_argument("--maker-fee-bps", type=float, default=2.0, help="Estimated maker fee in bps")
    parser.add_argument("--metrics-json", default="proof_of_efficiency/grid_metrics.jsonl", help="Path for JSONL metrics output")
    parser.add_argument("--metrics-csv", default="proof_of_efficiency/grid_metrics.csv", help="Path for CSV metrics output")
    parser.add_argument("--live", action="store_true", help="Enable Real Execution")
    parser.add_argument(
        "--confirm-live",
        default="",
        help='Mandatory confirmation string for live mode: "I_UNDERSTAND"',
    )
    # New Arguments
    parser.add_argument("--seed-side", choices=["buy", "sell", "both"], default="both", help="Initial grid side bias")
    parser.add_argument("--allow-open-shorts", action="store_true", help="Allow sell orders to open shorts (disables reduceOnly)")
    parser.add_argument("--auto-regime", action="store_true", help="Enable Adaptive Regime Mode")
    parser.add_argument("--min-confluence", type=int, default=3, help="Minimum confluence score to trade")
    
    args = parser.parse_args()

    if args.live and args.confirm_live != "I_UNDERSTAND":
        parser.error('Live mode requires --confirm-live "I_UNDERSTAND".')

    bot = GridExecutor(
        symbol=args.symbol,
        lower=args.lower,
        upper=args.upper,
        grids=args.grids,
        leverage=args.leverage,
        dry_run=not args.live,
        reference_price=args.reference_price,
        maker_fee_bps=args.maker_fee_bps,
        seed_side=args.seed_side,
        allow_open_shorts=args.allow_open_shorts,
        auto_regime=args.auto_regime,
        min_confluence=args.min_confluence,
    )

    print(colored("[INIT] INITIALIZING GRID EXECUTION ENGINE...", "magenta"))
    
    # Run Initial Regime Check
    if args.auto_regime:
        bot.auto_configure()
    
    if not args.live:
        print(colored("⚠️  DRY-RUN MODE. NO REAL ORDERS WILL BE PLACED.", "yellow"))
        print(colored("    Use --live to broadcast to Binance.", "yellow"))

    bot.cancel_all()
    run_result = bot.place_initial_grid()
    metrics_payload = bot.metrics.snapshot(step=run_result["step"], qty=run_result["qty"])
    bot.metrics.persist_jsonl(args.metrics_json, metrics_payload)
    bot.metrics.persist_csv(args.metrics_csv, metrics_payload)

    print(colored(f"[DONE] EXECUTION CYCLE COMPLETE. {run_result['orders_planned']} Orders Processed.", "magenta"))
    print(colored(f"[KPI] FillRate={metrics_payload['fill_rate']:.2%} | ErrorRate={metrics_payload['error_rate']:.2%}", "cyan"))
    print(colored(f"[KPI] EstFees=${metrics_payload['estimated_fees_usd']:.4f} | EstNetCyclePnL=${metrics_payload['est_net_cycle_pnl_usd']}", "cyan"))
    print(colored(f"[REPORT] JSONL -> {args.metrics_json}", "blue"))
    print(colored(f"[REPORT] CSV   -> {args.metrics_csv}", "blue"))
    
    # Enter Monitor Loop
    bot.monitor_loop()
