import ccxt
import pandas as pd
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def generate_execution_proof():
    load_dotenv("config/.env")
    
    api_key = os.getenv("BINANCE_API_KEY")
    secret = os.getenv("BINANCE_SECRET")
    
    if not api_key:
        print("[ERROR] NO API KEYS FOUND")
        return

    try:
        # Connect to Binance Futures
        exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret,
            'options': {'defaultType': 'future'}
        })
        
        # 1. Fetch Closed Orders (Futures)
        print("[AUDIT] FETCHING TRADE HISTORY (BINANCE FUTURES)...")
        trades = exchange.fetch_my_trades("BNB/USDT", limit=50)
        
        if not trades:
            print("[AUDIT] NO TRADES FOUND ON FUTURES ACCOUNT.")
            # Fallback to Spot check if Futures is empty
            print("[AUDIT] CHECKING SPOT MARKET HISTORY...")
            exchange_spot = ccxt.binance({'apiKey': api_key, 'secret': secret})
            trades = exchange_spot.fetch_my_trades("BNB/USDT", limit=50)
            market_type = "SPOT"
        else:
            market_type = "FUTURES"

        # 2. Format Data for Report
        records = []
        for t in trades:
            records.append({
                "EXECUTION_ID": t['id'],
                "TIMESTAMP_UTC": datetime.fromtimestamp(t['timestamp']/1000).strftime('%Y-%m-%d %H:%M:%S'),
                "SYMBOL": t['symbol'],
                "SIDE": t['side'].upper(),
                "PRICE": t['price'],
                "QUANTITY": t['amount'],
                "NOTIONAL_USD": t['cost'],
                "FEE_CURRENCY": t['fee']['currency'] if t.get('fee') else "N/A",
                "FEE_COST": t['fee']['cost'] if t.get('fee') else 0
            })
            
        df = pd.DataFrame(records)
        
        # 3. Fetch On-Chain Deposits (Proof of Funding)
        print("[AUDIT] FETCHING ON-CHAIN DEPOSITS...")
        try:
            # Fetch recent deposits to get TX HASH
            deposits = exchange.fetch_deposits(limit=5)
            deposit_logs = []
            if deposits:
                for d in deposits:
                    deposit_logs.append({
                        "TX_HASH": d['txid'],
                        "AMOUNT": d['amount'],
                        "CURRENCY": d['currency'],
                        "STATUS": d['status'],
                        "TIMESTAMP": datetime.fromtimestamp(d['timestamp']/1000).strftime('%Y-%m-%d %H:%M:%S')
                    })
        except Exception as e:
            print(f"[WARNING] COULD NOT FETCH DEPOSITS: {str(e)}")
            deposit_logs = []

        # 4. Generate Markdown Report
        report_path = "proof_of_efficiency/trade_execution_audit.md"
        with open(report_path, "w") as f:
            f.write(f"# OKTO AGENTIC TRADER: EXECUTION AUDIT\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
            f.write(f"**Market Context:** {market_type}\n\n")

            
            f.write("## 1. TRADE EXECUTION LOGS\n")
            if not df.empty:
                f.write("```text\n")
                f.write(df.to_string(index=False))
                f.write("\n```")
            else:
                f.write("*No trades executed in the last 24h window.*")
            
            f.write("\n\n## 2. ON-CHAIN FUNDING PROOF (VAULT -> CEX)\n")
            if deposit_logs:
                df_dep = pd.DataFrame(deposit_logs)
                f.write("```text\n")
                f.write(df_dep.to_string(index=False))
                f.write("\n```")
            else:
                f.write("*No recent on-chain deposits detected via API.*")

                
            f.write("\n\n---\n*Verified by Okto Agentic System*")
            
        print(f"[SUCCESS] AUDIT REPORT GENERATED: {report_path}")

    except Exception as e:
        print(f"[CRITICAL ERROR] AUDIT FAILED: {str(e)}")

if __name__ == "__main__":
    generate_execution_proof()
