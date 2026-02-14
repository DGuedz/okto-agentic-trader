import ccxt
import os
import sys
from termcolor import colored
from dotenv import load_dotenv

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def check_futures_connection():
    load_dotenv("config/.env")
    
    api_key = os.getenv("BINANCE_API_KEY")
    secret = os.getenv("BINANCE_SECRET")
    
    try:
        exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret,
            'enableRateLimit': True,
            'options': {'defaultType': 'future'}
        })
        
        # 1. Fetch Futures Balance
        balance = exchange.fetch_balance()
        usdt_free = balance['USDT']['free']
        print(colored(f"💰 FUTURES BALANCE: ${usdt_free:.2f} USDT", "green", attrs=['bold']))
        
        # 2. Check Permissions
        print("🔍 Checking Trading Permissions...")
        try:
            exchange.set_leverage(5, "BNB/USDT")
            print(colored("✅ Leverage Set OK (5x)", "green"))
        except Exception as e:
            print(colored(f"❌ Leverage Set Failed: {str(e)}", "red"))
            
        print(colored("🚀 SYSTEM READY FOR LAUNCH", "cyan", attrs=['bold']))

    except Exception as e:
        print(colored(f"❌ CONNECTION ERROR: {str(e)}", "red"))

if __name__ == "__main__":
    check_futures_connection()
