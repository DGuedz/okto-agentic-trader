import ccxt
import os
import sys
from termcolor import colored
from dotenv import load_dotenv

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def get_deposit_address():
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
        
        # Fetch deposit address for BNB
        # Note: network might need to be specified as 'BSC' or 'BNB'
        try:
            address_info = exchange.fetch_deposit_address('BNB', params={'network': 'BSC'})
            print(colored(f"🏦 BINANCE DEPOSIT ADDRESS (BSC):", "cyan", attrs=['bold']))
            print(colored(f"Address: {address_info['address']}", "green"))
            if 'tag' in address_info and address_info['tag']:
                print(colored(f"Memo/Tag: {address_info['tag']}", "yellow"))
        except Exception as e:
            print(colored(f"⚠️ Could not fetch specific BSC address: {str(e)}", "yellow"))
            # Try generic fetch
            address_info = exchange.fetch_deposit_address('BNB')
            print(colored(f"Address: {address_info}", "white"))

    except Exception as e:
        print(colored(f"❌ Error fetching deposit address: {str(e)}", "red"))

if __name__ == "__main__":
    get_deposit_address()
