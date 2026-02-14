import ccxt
import os
import sys
from termcolor import colored
from dotenv import load_dotenv

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def execute_spot_sell():
    load_dotenv("config/.env")
    
    api_key = os.getenv("BINANCE_API_KEY")
    secret = os.getenv("BINANCE_SECRET")
    
    try:
        exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret,
            'enableRateLimit': True,
            'options': {'defaultType': 'spot'}
        })
        
        # 1. Fetch Balance
        balance = exchange.fetch_balance()
        bnb_free = balance['BNB']['free']
        
        print(colored(f"💰 CURRENT HOLDING: {bnb_free:.6f} BNB", "cyan", attrs=['bold']))
        
        if bnb_free < 0.01:
            print(colored("⚠️ Balance too low to trade (Min ~0.01 BNB)", "yellow"))
            return

        # 2. Market Sell
        symbol = "BNB/USDT"
        print(colored(f"📉 EXECUTING MARKET SELL: {bnb_free} BNB -> USDT", "yellow"))
        
        order = exchange.create_market_sell_order(symbol, bnb_free)
        
        print(colored("✅ SELL EXECUTED!", "green", attrs=['bold']))
        print(f"Order ID: {order['id']}")
        print(f"Filled: {order['amount']} BNB")
        
        # 3. Check New USDT Balance
        time.sleep(1)
        new_balance = exchange.fetch_balance()
        usdt_free = new_balance['USDT']['free']
        print(colored(f"💵 NEW BALANCE: ${usdt_free:.2f} USDT", "green", attrs=['bold']))

    except Exception as e:
        print(colored(f"❌ SELL FAILED: {str(e)}", "red"))

if __name__ == "__main__":
    import time
    execute_spot_sell()
