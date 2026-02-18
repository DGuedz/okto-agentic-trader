import csv
import json
import os
import time
from datetime import datetime, timezone


class GridRunMetrics:
    def __init__(self, symbol, mode, leverage, maker_fee_bps=2.0):
        self.symbol = symbol
        self.mode = mode
        self.leverage = leverage
        self.maker_fee_bps = float(maker_fee_bps)
        self.started_at = time.time()
        self.run_id = f"grid-{int(self.started_at)}"

        self.attempted_orders = 0
        self.successful_orders = 0
        self.failed_orders = 0
        self.buy_attempts = 0
        self.sell_attempts = 0
        self.buy_success = 0
        self.sell_success = 0
        self.success_notional = 0.0
        self.estimated_fees = 0.0
        self.est_gross_cycle_pnl_usd = 0.0 # Initialize to 0.0
        self.est_net_cycle_pnl_usd = 0.0   # Initialize to 0.0
        self.errors = []
        self.strategy_context = {}

    def set_context(self, ctx):
        self.strategy_context = dict(ctx or {})

    def record_attempt(self, side):
        self.attempted_orders += 1
        if side == "buy":
            self.buy_attempts += 1
        elif side == "sell":
            self.sell_attempts += 1

    def record_success(self, side, price, amount):
        self.successful_orders += 1
        if side == "buy":
            self.buy_success += 1
        elif side == "sell":
            self.sell_success += 1

        notional = float(price) * float(amount)
        self.success_notional += notional
        # self.estimated_fees += notional * (self.maker_fee_bps / 10000.0) # Move fee calc to fill

    def record_fill(self, side, price, amount, pnl=0.0):
        # Record actual fill event
        notional = float(price) * float(amount)
        fee = notional * (self.maker_fee_bps / 10000.0)
        self.estimated_fees += fee
        
        # Add Cycle PnL
        # est_gross_cycle_pnl_usd tracks realized profit from closed cycles
        if pnl > 0:
            if self.est_gross_cycle_pnl_usd is None:
                self.est_gross_cycle_pnl_usd = 0.0
            self.est_gross_cycle_pnl_usd += pnl
            
            if self.est_net_cycle_pnl_usd is None:
                self.est_net_cycle_pnl_usd = 0.0
            self.est_net_cycle_pnl_usd += (pnl - fee) # Fee is deducted from gross PnL
        else:
             # Just fee deduction for opening trade
             if self.est_net_cycle_pnl_usd is not None:
                 self.est_net_cycle_pnl_usd -= fee

    def record_error(self, side, price, amount, error_message):
        self.failed_orders += 1
        self.errors.append(
            {
                "side": side,
                "price": float(price),
                "amount": float(amount),
                "error": str(error_message),
            }
        )

    def snapshot(self, step=None, qty=None):
        elapsed = max(0.0, time.time() - self.started_at)
        fill_rate = (self.successful_orders / self.attempted_orders) if self.attempted_orders else 0.0
        error_rate = (self.failed_orders / self.attempted_orders) if self.attempted_orders else 0.0

        return {
            "run_id": self.run_id,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "symbol": self.symbol,
            "mode": self.mode,
            "leverage": self.leverage,
            "maker_fee_bps": self.maker_fee_bps,
            "duration_sec": round(elapsed, 3),
            "attempted_orders": self.attempted_orders,
            "successful_orders": self.successful_orders,
            "failed_orders": self.failed_orders,
            "buy_attempts": self.buy_attempts,
            "sell_attempts": self.sell_attempts,
            "buy_success": self.buy_success,
            "sell_success": self.sell_success,
            "fill_rate": round(fill_rate, 6),
            "error_rate": round(error_rate, 6),
            "success_notional_usd": round(self.success_notional, 6),
            "estimated_fees_usd": round(self.estimated_fees, 6),
            "est_gross_cycle_pnl_usd": round(self.est_gross_cycle_pnl_usd, 6),
            "est_net_cycle_pnl_usd": round(self.est_net_cycle_pnl_usd, 6),
            "strategy_context": self.strategy_context,
            "errors": self.errors,
        }

    @staticmethod
    def _ensure_parent(path):
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)

    def persist_jsonl(self, path, payload):
        self._ensure_parent(path)
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=True) + "\n")

    def persist_csv(self, path, payload):
        self._ensure_parent(path)
        flat_payload = dict(payload)
        flat_payload["errors"] = json.dumps(payload.get("errors", []), ensure_ascii=True)
        fieldnames = list(flat_payload.keys())
        file_exists = os.path.exists(path)
        with open(path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(flat_payload)
