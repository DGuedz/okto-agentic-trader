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

    # print(colored("🔍 CHECKING TREASURY (SPOT + FUTURES)...", "cyan"))

    total_equity = 0
    spot_usdt = 0
    futures_usdt = 0
    pnl_unrealized = 0

    # 1. Check SPOT Wallet
    try:
        spot_exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret,
            'enableRateLimit': True,
            'options': {'defaultType': 'spot'}
        })
        
        spot_balance = spot_exchange.fetch_balance()
        spot_usdt = spot_balance['USDT']['total']
        spot_bnb = spot_balance['BNB']['total']
        
        # Get current BNB Price for conversion
        ticker = spot_exchange.fetch_ticker('BNB/USDT')
        bnb_price = ticker['last']
        
        spot_val = spot_usdt + (spot_bnb * bnb_price)
        
    except Exception as e:
        spot_val = 0
        bnb_price = 0

    # 2. Check FUTURES Wallet
    try:
        futures_exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret,
            'enableRateLimit': True,
            'options': {'defaultType': 'future'}
        })
        
        futures_balance = futures_exchange.fetch_balance()
        futures_usdt = futures_balance['USDT']['total']
        futures_bnb = futures_balance['BNB']['total'] if 'BNB' in futures_balance else 0
        
        # Check Open Positions for Unrealized PnL
        positions = futures_exchange.fetch_positions()
        active_positions = [p for p in positions if float(p['contracts']) > 0]
        
        if active_positions:
            for p in active_positions:
                pnl_unrealized += float(p['unrealizedPnl'])
        
        futures_val = futures_usdt + (futures_bnb * bnb_price) + pnl_unrealized

    except Exception as e:
        futures_val = 0

    # 3. Total Aggregation
    total_equity = spot_val + futures_val
    
    print(colored(f"💰 TREASURY STATUS:", "cyan", attrs=['bold']))
    print(colored(f"💵 SPOT:    ${spot_val:.2f}", "white"))
    print(colored(f"🚀 FUTURES: ${futures_val:.2f}", "magenta"))
    if pnl_unrealized != 0:
        pnl_color = "green" if pnl_unrealized >= 0 else "red"
        print(colored(f"📊 OPEN PnL: ${pnl_unrealized:.2f}", pnl_color))
        
    print(colored(f"💎 TOTAL EQUITY: ${total_equity:.2f}", "white", attrs=['bold']))

    # Mission Control HUD
    from ops.mission_control import MissionControl
    mission = MissionControl()
    mission.print_hud(total_equity)

if __name__ == "__main__":
    check_treasury()
