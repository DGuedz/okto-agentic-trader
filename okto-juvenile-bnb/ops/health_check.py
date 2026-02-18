import argparse
import json
import os
import sys
from datetime import datetime, timezone

import ccxt
from dotenv import load_dotenv

def utc_now_iso():
    return datetime.now(timezone.utc).isoformat()

def parse_jsonl_last(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"metrics file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines:
        raise ValueError("metrics file is empty")
    return json.loads(lines[-1])

def fetch_live_state(symbol):
    load_dotenv("config/.env")
    api_key = os.getenv("BINANCE_API_KEY")
    secret = os.getenv("BINANCE_SECRET")
    if not api_key or not secret:
        raise RuntimeError("missing BINANCE_API_KEY/BINANCE_SECRET")

    ex = ccxt.binance(
        {
            "apiKey": api_key,
            "secret": secret,
            "enableRateLimit": True,
            "options": {"defaultType": "future"},
        }
    )

    bal = ex.fetch_balance()
    usdt_free = float(bal.get("USDT", {}).get("free", 0.0))
    open_orders = ex.fetch_open_orders(symbol)
    pos = ex.fetch_positions([symbol])
    contracts = 0.0
    unrealized = 0.0
    side = "flat"
    if pos:
        p = pos[0]
        contracts = float(p.get("contracts") or 0.0)
        unrealized = float(p.get("unrealizedPnl") or 0.0)
        if contracts > 0:
            side = p.get("side") or "long"

    return {
        "usdt_free": usdt_free,
        "open_orders": len(open_orders),
        "position_contracts": contracts,
        "position_side": side,
        "unrealized_pnl": unrealized,
    }

def classify(metrics, live_state, error_warn, error_crit, min_open_orders):
    reasons = []
    status = "GREEN"

    error_rate = float(metrics.get("error_rate", 0.0))
    fill_rate = float(metrics.get("fill_rate", 0.0))
    net_cycle = float(metrics.get("est_net_cycle_pnl_usd", 0.0))

    if error_rate >= error_crit:
        status = "RED"
        reasons.append(f"error_rate={error_rate:.2%} >= {error_crit:.2%}")
    elif error_rate >= error_warn:
        status = "YELLOW"
        reasons.append(f"error_rate={error_rate:.2%} >= {error_warn:.2%}")

    if fill_rate <= 0.0:
        # Warning but not critical if just started
        # status = "YELLOW" if status == "GREEN" else status
        reasons.append("fill_rate is zero (no fills yet)")

    if net_cycle < 0:
        status = "YELLOW" if status == "GREEN" else status
        reasons.append(f"est_net_cycle_pnl_usd={net_cycle:.6f} < 0")

    if live_state is not None:
        if live_state["open_orders"] < min_open_orders:
            status = "YELLOW" if status == "GREEN" else status
            reasons.append(
                f"open_orders={live_state['open_orders']} < min_open_orders={min_open_orders}"
            )
        if live_state["usdt_free"] < 2.0:
            status = "YELLOW" if status == "GREEN" else status
            reasons.append(f"low free margin usdt_free={live_state['usdt_free']:.4f}")

    if not reasons:
        reasons.append("all checks passed")
    return status, reasons

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", default="BNB/USDT:USDT")
    parser.add_argument(
        "--metrics-json", default="proof_of_efficiency/grid_metrics.jsonl"
    )
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--error-warn", type=float, default=0.02)
    parser.add_argument("--error-crit", type=float, default=0.10)
    parser.add_argument("--min-open-orders", type=int, default=1)
    args = parser.parse_args()

    try:
        metrics = parse_jsonl_last(args.metrics_json)
        live_state = None
        if not args.offline:
             live_state = fetch_live_state(args.symbol)
             
        status, reasons = classify(
            metrics,
            live_state,
            error_warn=args.error_warn,
            error_crit=args.error_crit,
            min_open_orders=args.min_open_orders,
        )

        payload = {
            "timestamp_utc": utc_now_iso(),
            "status": status,
            "symbol": args.symbol,
            "metrics": {
                "run_id": metrics.get("run_id"),
                "mode": metrics.get("mode"),
                "fill_rate": metrics.get("fill_rate"),
                "error_rate": metrics.get("error_rate"),
                "est_net_cycle_pnl_usd": metrics.get("est_net_cycle_pnl_usd"),
                "attempted_orders": metrics.get("attempted_orders"),
                "successful_orders": metrics.get("successful_orders"),
                "failed_orders": metrics.get("failed_orders"),
            },
            "live_state": live_state,
            "reasons": reasons,
        }
        print(json.dumps(payload, ensure_ascii=True, indent=2))
        if status == "RED":
            sys.exit(2)
    except Exception as e:
        print(json.dumps({"status": "RED", "error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
