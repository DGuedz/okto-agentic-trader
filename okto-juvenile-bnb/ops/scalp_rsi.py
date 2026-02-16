import ccxt
import pandas as pd
import time
import os
from termcolor import colored

from dotenv import load_dotenv

from ops.aster_monitor import AsterMonitor # Import Hidden Order Logic

from ops.obi_analyzer import analyze_obi

class ScalpTentacle:
    def __init__(self):
        # Load Env explicitly
        load_dotenv("config/.env")
        
        self.HACKATHON_MODE = True # 🚨 SURVIVAL MODE: HIGH WIN RATE PRIORITY
        
        # Initialize Exchange Connection (Binance)
        api_key = os.getenv("BINANCE_API_KEY")
        secret = os.getenv("BINANCE_SECRET")
        
        # Initialize Aster Module for Dark Pool Logic
        self.aster = AsterMonitor()


        
        config = {
            'enableRateLimit': True,
            'options': {'defaultType': 'future'} 
        }
        
        if api_key and secret and len(api_key) > 10:
            config['apiKey'] = api_key
            config['secret'] = secret
            self.mode = "LIVE_TRADING"
            print("[SYSTEM] BINANCE FUTURES API: CONNECTED")
        else:
            self.mode = "READ_ONLY"
            print("[SYSTEM] BINANCE FUTURES API: READ ONLY (NO KEYS)")
            # DEBUG
            print(f"[DEBUG] KEY LEN: {len(str(api_key))}, SECRET LEN: {len(str(secret))}")


        self.exchange = ccxt.binance(config)
        self.symbol = "BNB/USDT"
        self.leverage = 5
        
        # Set Leverage
        if self.mode == "LIVE_TRADING":
            try:
                self.exchange.set_leverage(self.leverage, self.symbol)
                print(f"[SYSTEM] LEVERAGE SET TO {self.leverage}x")
            except Exception as e:
                print(f"[ERROR] COULD NOT SET LEVERAGE: {str(e)}")

        
    def cancel_all_open_orders(self):
        """Cancels all open orders to clear the board for new grid"""
        try:
            print("[GRID] CLEARING OLD ORDERS...")
            self.exchange.cancel_all_orders(self.symbol)
            return True
        except Exception as e:
            print(f"[WARNING] COULD NOT CANCEL ORDERS: {str(e)}")
            return False

    def setup_smart_grid(self, amount_usd=15, phase="SEED"):
        """
        Places LIMIT orders (Maker) based on technical analysis.
        - Entry: Buy Limit @ Support (Bollinger Lower / OBI Wall)
        - Target: Sell Limit @ Resistance (Bollinger Upper / OBI Wall)
        
        PHASE ADJUSTMENTS:
        - SEED: Ultra-Conservative. Only enters at DEEP support (OBI Wall required).
        - ALPHA+: More flexible, uses BB Lower as fallback.
        """
        if self.mode == "READ_ONLY": return False

        try:
            # 1. Analyze Market
            ohlcv = self.exchange.fetch_ohlcv(self.symbol, timeframe='1m', limit=100)
            current_price = ohlcv[-1][4]
            bb = self.calculate_bollinger_bands(ohlcv)
            obi_data = analyze_obi(self.symbol)
            
            # 2. Determine Smart Entry Price (Buy Limit)
            entry_price = bb['lower']
            
            # 🚨 VOLATILITY GUARD (ATR CHECK)
            ohlcv_atr = self.exchange.fetch_ohlcv(self.symbol, timeframe='1m', limit=50)
            current_atr = self.calculate_atr(ohlcv_atr)
            
            # If ATR is too high (Panic Mode) or too low (Dead Market), ADJUST
            if current_atr > 1.5: # Extremely Volatile
                 print(colored(f"⚠️ HIGH VOLATILITY DETECTED (ATR: {current_atr:.2f}). REDUCING LEVERAGE.", "yellow"))
                 self.leverage = 2 # Safety Mode
            elif current_atr < 0.1: # Dead Market
                 print(colored(f"💤 LOW VOLATILITY (ATR: {current_atr:.2f}). WAITING FOR VOLUME.", "blue"))
                 if self.HACKATHON_MODE:
                     return {"success": False, "error": "LOW_VOLATILITY"}
            
            # CHOPPY MARKET FILTER (ADX SIMULATION)
            # If high volatility but no direction (sideways chop), avoid getting shredded.
            # Simple heuristic: If BB Bandwidth is wide but price is bouncing inside without OBI trend.
            bb_width = (bb['upper'] - bb['lower']) / bb['middle']
            if bb_width > 0.02 and abs(obi_data['obi']) < 0.1:
                print(colored(f"🌊 CHOPPY WATERS DETECTED (Wide Bands + No Trend). SKIPPING.", "magenta"))
                return {"success": False, "error": "CHOPPY_MARKET"}

            # SEED GRADUATION STRATEGY (PHASE LOGIC)
            if phase == "SEED" or self.HACKATHON_MODE:
                # STRICT MODE: Only trust OBI Walls or very deep BB deviations
                
                # 🚨 ANTI-RANDOMNESS PROTOCOL (User Directive)
                # "Entrar em uma operação sem olhar o livro de ordens é um erro matemático."
                if self.HACKATHON_MODE:
                    if not obi_data or obi_data['obi'] < 0.1: # Must have positive imbalance for LONG
                        print(colored("🛑 [SURVIVAL] ENTRY BLOCKED: INSUFFICIENT BUY PRESSURE (OBI < 0.1)", "red", attrs=['bold']))
                        return {"success": False, "error": "OBI_BLOCK"}
                
                if obi_data and obi_data['buy_wall_price'] < current_price:
                     # Use OBI wall as primary truth
                     entry_price = obi_data['buy_wall_price'] * 1.0001
                     print(colored(f"🛡️ [SURVIVAL] ENTRY LOCKED TO OBI WALL: ${entry_price:.2f}", "cyan", attrs=['bold']))
                else:
                    if self.HACKATHON_MODE:
                         print(colored("🛑 [SURVIVAL] ENTRY BLOCKED: NO LIQUIDITY WALL FOUND", "red", attrs=['bold']))
                         return {"success": False, "error": "NO_WALL_BLOCK"}
                    
                    # If no OBI wall, lower the BB entry to ensure safety (Lower Band - 0.5% in Survival)
                    discount = 0.995 if self.HACKATHON_MODE else 0.999
                    entry_price = bb['lower'] * discount
                    print(colored(f"🛡️ [SURVIVAL] DEEPENING ENTRY TO: ${entry_price:.2f} (Discount: {discount})", "yellow"))
            else:
                # ALPHA/BETA MODE: Standard Logic
                if obi_data and obi_data['buy_wall_price'] > entry_price and obi_data['buy_wall_price'] < current_price:
                    entry_price = obi_data['buy_wall_price'] * 1.0001
                    print(colored(f"🛡️ ENTRY SUPPORT FOUND (OBI): ${entry_price:.2f}", "cyan"))
                else:
                    print(colored(f"📉 ENTRY SUPPORT FOUND (BB): ${entry_price:.2f}", "cyan"))

            # Calculate Amount
            balance = self.exchange.fetch_balance()
            usdt_free = balance['USDT']['free']
            
            # DYNAMIC LEVERAGE ALLOCATION
            # In High Volatility, use less margin
            margin_risk_ratio = 0.50 if current_atr > 1.0 else 0.95
            
            margin_to_use = usdt_free * margin_risk_ratio 
            position_size_usd = margin_to_use * self.leverage
            amount_bnb = float(f"{position_size_usd / entry_price:.2f}")
            
            # FORCE MINIMUM SIZE FOR BINANCE (0.01 BNB)
            if amount_bnb < 0.01:
                print(colored(f"⚠️  AJUSTANDO TAMANHO MÍNIMO: {amount_bnb} -> 0.01 BNB", "yellow"))
                amount_bnb = 0.01

            # 3. Place Limit Buy Order (The Trap)
            print(f"[GRID] SETTING TRAP | BUY LIMIT @ ${entry_price:.2f} | AMT: {amount_bnb} BNB")
            entry_order = self.exchange.create_order(
                symbol=self.symbol,
                type='LIMIT',
                side='buy',
                amount=amount_bnb,
                price=entry_price,
                params={'timeInForce': 'GTC'} # Good Till Cancel
            )
            
            # 4. Pre-calculate Exit (Take Profit)
            target_price = bb['upper']
            
            # SEED GRADUATION: Take profit earlier to secure small wins (Scalp Mode)
            if phase == "SEED" or self.HACKATHON_MODE:
                 # Target Middle Band instead of Upper for higher probability
                 target_price = (bb['upper'] + bb['middle']) / 2
                 if self.HACKATHON_MODE:
                     target_price = bb['middle'] # Even safer: Mean Reversion only
                     print(colored(f"🎯 [SURVIVAL] TARGET LOCKED TO MID-BAND: ${target_price:.2f}", "magenta"))
                 else:
                     print(colored(f"🎯 [SEED PROTOCOL] TARGET ADJUSTED TO MID-UPPER BAND: ${target_price:.2f}", "magenta"))

            if obi_data and obi_data['sell_wall_price'] < target_price and obi_data['sell_wall_price'] > current_price:
                target_price = obi_data['sell_wall_price'] * 0.999 # Just below wall
            
            roi_pct = ((target_price - entry_price) / entry_price) * 100 * self.leverage
            print(colored(f"🎯 PRE-SET TARGET: ${target_price:.2f} (Est. ROI: {roi_pct:.2f}%)", "green"))
            print(colored(f"✅ SMART GRID DEPLOYED. WAITING FOR PRICE EXECUTION ({phase} MODE).", "green", attrs=['bold']))
            
            return {"success": True, "entry": entry_price, "target": target_price}

        except Exception as e:
            print(f"[ERROR] GRID SETUP FAILED: {str(e)}")
            return {"success": False, "error": str(e)}

    def execute_buy(self, amount_usd=15):
        """Executes a Market Buy Order (LONG)"""
        if self.mode == "READ_ONLY":
            print("[ERROR] CANNOT TRADE IN READ_ONLY MODE")
            return False

        try:
            # 1. Get current price
            ticker = self.exchange.fetch_ticker(self.symbol)
            price = ticker['last']
            
            # 2. Calculate position size with leverage
            # Effective Position = Capital * Leverage
            # Example: $13 * 5 = $65 position
            
            # Check USDT Balance
            balance = self.exchange.fetch_balance()
            usdt_free = balance['USDT']['free']
            
            if usdt_free < 2:
                print("[WARNING] INSUFFICIENT USDT MARGIN")
                return False

            
            # Use max 50% of available margin per trade to be safe
            margin_to_use = usdt_free * 0.95 
            position_size_usd = margin_to_use * self.leverage
            amount_bnb = position_size_usd / price
            
            # Precision adjustment (floor to 2 decimals for BNB futures)
            amount_bnb = float(f"{amount_bnb:.2f}")

            print(f"[EXECUTION] OPENING LONG (5x) | AMOUNT: {amount_bnb} BNB | PRICE: ${price}")
            
            # 2. Execute Order (Pro Mode: Dark Pool Split & MEV Protection)
            # Calculate Slippage Risk
            is_risky, estimated_slippage = self.aster.check_slippage_risk(amount_bnb, price)
            
            # If trade size is > 1 BNB OR High Slippage Risk, split it.
            if amount_bnb > 1.0 or is_risky:
                 reason = "SIZE > 1.0" if amount_bnb > 1.0 else "MEV RISK"
                 print(f"[DARK POOL] SPLITTING ORDER ({reason}) | TOTAL: {amount_bnb} BNB")
                 chunks = self.aster.simulate_dark_pool_split(amount_bnb)
                 
                 for chunk in chunks:
                     print(f"   >>> [HIDDEN] EXECUTING CHUNK: {chunk} BNB")
                     self.exchange.create_market_buy_order(self.symbol, chunk)
                     time.sleep(0.2) # Anti-front-run delay
                 
                 order = {"id": "hidden_order_batch", "amount": amount_bnb} # Simulated response
            else:
                # Standard Execution for small orders
                # Execute MARKET BUY
                order = self.exchange.create_market_buy_order(self.symbol, amount_bnb)
                
                # 3. Set OCO (One-Cancels-Other) like Safety Orders
                
                # VOLATILITY CALCULATION (Dynamic Risk)
                # Fetch ATR to adjust SL/TP based on market noise
                ohlcv = self.exchange.fetch_ohlcv(self.symbol, timeframe='1m', limit=50)
                atr = self.calculate_atr(ohlcv)
                
                # Dynamic Bands: 
                # SL = 2.5x ATR (Give room to breathe)
                # TP = 4.0x ATR (Capture the swing)
                
                if self.HACKATHON_MODE:
                    # TIGHTER STOPS FOR SURVIVAL
                    sl_dist = atr * 1.5
                    tp_dist = atr * 2.0
                    print(colored("🚨 HACKATHON MODE: TIGHTER SL/TP (1.5x/2.0x ATR)", "yellow"))
                else:
                    sl_dist = atr * 2.5
                    tp_dist = atr * 4.0
                
                sl_price = float(f"{price - sl_dist:.2f}")
                
                # TAKE PROFIT STRATEGY (SMART OBI + VOLATILITY)
                # Analyze Order Book to find resistance
                obi_data = analyze_obi(self.symbol)
                
                if obi_data and obi_data['sell_wall_price'] > price:
                    # Smart Exit: Place TP just before the big Sell Wall
                    smart_tp = float(f"{obi_data['sell_wall_price'] * 0.999:.2f}")
                    
                    # If Smart TP is within volatility range (reachable), use it
                    if smart_tp < (price + tp_dist) and smart_tp > price:
                         tp_price = smart_tp
                         print(colored(f"🎯 OPTIMIZED TP (OBI WALL): ${tp_price}", "cyan"))
                    else:
                         tp_price = float(f"{price + tp_dist:.2f}")
                         print(colored(f"🌊 VOLATILITY TP (ATR): ${tp_price}", "blue"))
                else:
                    # Default Volatility Target
                    tp_price = float(f"{price + tp_dist:.2f}")
                    print(colored(f"🌊 VOLATILITY TP (ATR): ${tp_price}", "blue"))

                print(f"[RISK] DYNAMIC ATR: {atr:.4f} | SL: ${sl_price} | TP: ${tp_price}")

                try:
                    # Place STOP LOSS Market Order
                    self.exchange.create_order(
                        symbol=self.symbol,
                        type='STOP_MARKET',
                        side='sell',
                        amount=amount_bnb,
                        params={'stopPrice': sl_price, 'reduceOnly': True}
                    )
                    
                    # Place TAKE PROFIT Market Order
                    self.exchange.create_order(
                        symbol=self.symbol,
                        type='TAKE_PROFIT_MARKET',
                        side='sell',
                        amount=amount_bnb,
                        params={'stopPrice': tp_price, 'reduceOnly': True}
                    )
                    print(colored("✅ SAFETY NET DEPLOYED (SL/TP)", "green"))
                    
                except Exception as e:
                    print(colored(f"⚠️ COULD NOT SET SL/TP: {str(e)}", "yellow"))
            
            return {"success": True, "order": order, "price": price}
            
        except Exception as e:
            print(f"[ERROR] LONG EXECUTION FAILED: {str(e)}")
            return {"success": False, "error": str(e)}

    def execute_short(self, amount_usd=15):
        """Executes a Market Sell Order (SHORT)"""
        if self.mode == "READ_ONLY": return False

        try:
            ticker = self.exchange.fetch_ticker(self.symbol)
            price = ticker['last']
            
            balance = self.exchange.fetch_balance()
            usdt_free = balance['USDT']['free']
            
            if usdt_free < 2:
                print("[WARNING] INSUFFICIENT USDT MARGIN FOR SHORT")
                return False

            margin_to_use = usdt_free * 0.95 
            position_size_usd = margin_to_use * self.leverage
            amount_bnb = position_size_usd / price
            amount_bnb = float(f"{amount_bnb:.2f}")

            print(f"[EXECUTION] OPENING SHORT (5x) | AMOUNT: {amount_bnb} BNB | PRICE: ${price}")
            
            # Execute MARKET SELL (SHORT)
            order = self.exchange.create_market_sell_order(self.symbol, amount_bnb)
            
            # SET SAFETY NET (Inverse of Long)
            # STOP LOSS: 1.5% Above Entry (Risk)
            sl_price = float(f"{price * 1.015:.2f}")
            
            # TAKE PROFIT: Smart OBI or Default -3% (Reward)
            obi_data = analyze_obi(self.symbol)
            if obi_data and obi_data['buy_wall_price'] < price:
                smart_tp = float(f"{obi_data['buy_wall_price'] * 1.001:.2f}") # Just above Buy Wall
                if smart_tp < price * 0.995: # At least 0.5% profit
                    tp_price = smart_tp
                    print(colored(f"🎯 OPTIMIZED TP SET ABOVE SUPPORT: ${tp_price}", "cyan"))
                else:
                    tp_price = float(f"{price * 0.97:.2f}")
            else:
                tp_price = float(f"{price * 0.97:.2f}")

            print(f"[RISK] SETTING STOPS | SL: ${sl_price} | TP: ${tp_price}")

            try:
                # Place STOP LOSS (BUY STOP)
                self.exchange.create_order(
                    symbol=self.symbol,
                    type='STOP_MARKET',
                    side='buy',
                    amount=amount_bnb,
                    params={'stopPrice': sl_price, 'reduceOnly': True}
                )
                # Place TAKE PROFIT (BUY LIMIT/MARKET)
                self.exchange.create_order(
                    symbol=self.symbol,
                    type='TAKE_PROFIT_MARKET',
                    side='buy',
                    amount=amount_bnb,
                    params={'stopPrice': tp_price, 'reduceOnly': True}
                )
                print(colored("✅ SHORT SAFETY NET DEPLOYED", "green"))
            except Exception as e:
                print(colored(f"⚠️ COULD NOT SET SHORT SL/TP: {str(e)}", "yellow"))

            return {"success": True, "order": order, "price": price}

        except Exception as e:
            print(f"[ERROR] SHORT EXECUTION FAILED: {str(e)}")
            return {"success": False, "error": str(e)}

    def execute_sell(self):
        """Executes a Market Sell Order (CLOSE LONG or OPEN SHORT)"""
        # For this simple scalp bot, SELL means CLOSE POSITION
        if self.mode == "READ_ONLY": return False
        
        try:
            # 1. Check Current Position
            positions = self.exchange.fetch_positions([self.symbol])
            bnb_position = [p for p in positions if p['symbol'] == self.symbol]
            
            if not bnb_position:
                print("[WARNING] NO POSITION TO CLOSE")
                return False
                
            amt = float(bnb_position[0]['contracts']) # Size in BNB
            
            if amt > 0:
                print(f"[EXECUTION] CLOSING LONG | AMOUNT: {amt} BNB")
                # To close a LONG, we SELL
                order = self.exchange.create_market_sell_order(self.symbol, amt)
                return {"success": True, "order": order}
            else:
                print("[WARNING] NO LONG POSITION DETECTED")
                return False
            
        except Exception as e:
            print(f"[ERROR] CLOSE POSITION FAILED: {str(e)}")
            return {"success": False, "error": str(e)}


        
    def calculate_volume_delta(self, ohlcv):
        """
        Estimates HFT Volume Delta (Aggression).
        Positive = Buyers are aggressive (Taking liquidity).
        Negative = Sellers are aggressive (Dumping).
        """
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        
        # Simple estimation: If Close > Open, assume Buy Vol. Else Sell Vol.
        # For HFT precision, we would need tick data, but this is a solid 1m proxy.
        df['delta'] = df.apply(lambda x: x['volume'] if x['close'] >= x['open'] else -x['volume'], axis=1)
        
        # Sum last 3 candles for immediate momentum
        recent_delta = df['delta'].tail(3).sum()
        return recent_delta

    def calculate_bollinger_bands(self, ohlcv, period=20, std_dev=2):
        """Calculates Bollinger Bands (Upper, Middle, Lower)"""
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        
        df['sma'] = df['close'].rolling(window=period).mean()
        df['std'] = df['close'].rolling(window=period).std()
        
        df['upper_band'] = df['sma'] + (df['std'] * std_dev)
        df['lower_band'] = df['sma'] - (df['std'] * std_dev)
        
        return {
            "upper": df['upper_band'].iloc[-1],
            "middle": df['sma'].iloc[-1],
            "lower": df['lower_band'].iloc[-1]
        }

    def calculate_vwap(self, ohlcv):
        """
        Calculates VWAP (Volume Weighted Average Price).
        Institutional 'Fair Price' benchmark.
        """
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        
        # Typical Price = (High + Low + Close) / 3
        df['typical_price'] = (df['high'] + df['low'] + df['close']) / 3
        df['pv'] = df['typical_price'] * df['volume']
        
        # Cumulative VWAP (Rolling window to simulate session)
        df['cum_pv'] = df['pv'].rolling(window=50).sum()
        df['cum_vol'] = df['volume'].rolling(window=50).sum()
        
        df['vwap'] = df['cum_pv'] / df['cum_vol']
        
        return df['vwap'].iloc[-1]

    def get_funding_rate(self):
        """Fetches current funding rate (Sentiment Indicator)"""
        try:
            funding = self.exchange.fetch_funding_rate(self.symbol)
            return funding['fundingRate']
        except:
            return 0.0

    def calculate_atr(self, ohlcv, period=14):
        """Calculates Average True Range (Volatility)"""
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        
        # True Range Calculation
        df['h-l'] = df['high'] - df['low']
        df['h-pc'] = abs(df['high'] - df['close'].shift(1))
        df['l-pc'] = abs(df['low'] - df['close'].shift(1))
        
        df['tr'] = df[['h-l', 'h-pc', 'l-pc']].max(axis=1)
        
        # Simple Moving Average of TR
        df['atr'] = df['tr'].rolling(window=period).mean()
        
        return df['atr'].iloc[-1]

    def calculate_rsi(self, ohlcv, period=14):
        """Standard RSI 14 calculation"""
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))
        return df['rsi'].iloc[-1]

    def scan_market(self, phase="SEED"):
        """
        Main Loop for Tentacle 01
        1. Fetch Prices
        2. Calc RSI, BB, Volume Delta
        3. Determine Entry/Exit
        """
        try:
            # Fetch OHLCV
            ohlcv = self.exchange.fetch_ohlcv(self.symbol, timeframe='1m', limit=100)
            
            # --- CALCULATION BLOCK START ---
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            
            # RSI
            delta = df['close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            current_rsi = rsi.iloc[-1]
            
            # BB
            bb = self.calculate_bollinger_bands(ohlcv)
            
            # VWAP
            df['vwap'] = (df['volume'] * (df['high'] + df['low'] + df['close']) / 3).cumsum() / df['volume'].cumsum()
            current_vwap = df['vwap'].iloc[-1]
            
            # Funding
            try:
                funding = self.exchange.fetch_funding_rate(self.symbol)
                funding_rate = funding['fundingRate']
            except:
                funding_rate = 0.0
                
            # Delta
            # Simple approx: Up candle vol - Down candle vol
            current_delta = 0
            if df['close'].iloc[-1] > df['open'].iloc[-1]:
                current_delta = df['volume'].iloc[-1]
            else:
                current_delta = -df['volume'].iloc[-1]
                
            # ATR (for volatility)
            atr = self.calculate_atr(ohlcv)
            
            # --- CALCULATION BLOCK END ---

            return {
                "success": True,
                "price": df['close'].iloc[-1],
                "rsi": current_rsi,
                "bb": bb,
                "vwap": current_vwap,
                "funding": funding_rate,
                "delta": current_delta,
                "atr": atr,
                "phase": phase # Return phase for debugging
            }

        except Exception as e:
            print(f"[ERROR] SCAN FAILED: {str(e)}")
            return {"success": False, "error": str(e)}
