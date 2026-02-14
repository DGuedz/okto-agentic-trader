import ccxt
import os
import sys
from termcolor import colored
from dotenv import load_dotenv

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def transfer_spot_to_future():
    load_dotenv("config/.env")
    
    api_key = os.getenv("BINANCE_API_KEY")
    secret = os.getenv("BINANCE_SECRET")
    
    try:
        exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret,
            'enableRateLimit': True
        })
        
        # 1. Fetch Spot USDT Balance
        balance = exchange.fetch_balance()
        usdt_free = balance['USDT']['free']
        
        print(colored(f"💵 SPOT BALANCE: ${usdt_free:.2f} USDT", "cyan", attrs=['bold']))
        
        if usdt_free < 1:
            print(colored("⚠️ Balance too low to transfer (Min $1)", "yellow"))
            return

        # 2. Transfer to Futures (USDT-M)
        # Type 1: Spot to USDT-M Futures
        print(colored(f"🔄 TRANSFERRING {usdt_free:.2f} USDT TO FUTURES...", "yellow"))
        
        try:
            # Universal Transfer Endpoint
            transfer = exchange.sapi_post_asset_transfer({
                'type': 'MAIN_UMFUTURE', # Main account to USDT-M Futures
                'asset': 'USDT',
                'amount': usdt_free
            })
            print(colored("✅ TRANSFER SUCCESSFUL!", "green", attrs=['bold']))
            print(f"Transfer ID: {transfer['tranId']}")
            
        except Exception as e:
            print(colored(f"⚠️ API Transfer Failed (Permissions?): {str(e)}", "red"))
            print(colored("👉 Please transfer manually in the Binance App: Wallets -> Transfer -> Spot to Futures", "white"))

    except Exception as e:
        print(colored(f"❌ ERROR: {str(e)}", "red"))

if __name__ == "__main__":
    transfer_spot_to_future()
