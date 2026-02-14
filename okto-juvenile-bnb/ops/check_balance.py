import ccxt
import os
import sys
from termcolor import colored
from dotenv import load_dotenv

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def check_treasury():
    load_dotenv("config/.env")
    
    api_key = os.getenv("BINANCE_API_KEY")
    secret = os.getenv("BINANCE_SECRET")
    
    if not api_key or not secret:
        print(colored("❌ Missing Binance API Keys", "red"))
        return

    try:
        exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret,
            'enableRateLimit': True
        })
        
        balance = exchange.fetch_balance()
        
        usdt = balance['USDT']['free']
        bnb = balance['BNB']['free']
        
        print(colored(f"💰 TREASURY STATUS:", "cyan", attrs=['bold']))
        print(colored(f"💵 USDT: ${usdt:.2f}", "green"))
        print(colored(f"🔶 BNB:  {bnb:.6f}", "yellow"))
        
        # Estimate total in USD
        ticker = exchange.fetch_ticker('BNB/USDT')
        price = ticker['last']
        total_usd = usdt + (bnb * price)
        
        print(colored(f"📊 TOTAL EQUITY: ${total_usd:.2f}", "white", attrs=['bold']))
        
    except Exception as e:
        print(colored(f"❌ Error fetching balance: {str(e)}", "red"))

if __name__ == "__main__":
    check_treasury()
