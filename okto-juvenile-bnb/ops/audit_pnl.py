import ccxt
import os
import sys
from termcolor import colored
from dotenv import load_dotenv

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def audit_pnl():
    load_dotenv("config/.env")
    
    api_key = os.getenv("BINANCE_API_KEY")
    secret = os.getenv("BINANCE_SECRET")
    
    if not api_key or not secret:
        print(colored("❌ Missing Binance API Keys", "red"))
        return

    print(colored("🔍 STARTING FORENSIC PnL AUDIT...", "cyan", attrs=['bold']))

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
        
        print(colored("\n[SPOT WALLET]", "yellow"))
        print(f"💵 USDT: ${spot_usdt:.2f}")
        print(f"🔶 BNB:  {spot_bnb:.6f}")
        
    except Exception as e:
        print(colored(f"❌ Error fetching SPOT balance: {str(e)}", "red"))
        spot_usdt = 0
        spot_bnb = 0

    # 2. Check FUTURES Wallet
    try:
        futures_exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret,
            'enableRateLimit': True,
            'options': {'defaultType': 'future'}
        })
        
        futures_balance = futures_exchange.fetch_balance()
        # In futures, 'USDT' is usually the collateral
        futures_usdt = futures_balance['USDT']['total']
        futures_bnb = futures_balance['BNB']['total'] if 'BNB' in futures_balance else 0
        
        print(colored("\n[FUTURES WALLET]", "magenta"))
        print(f"💵 USDT: ${futures_usdt:.2f}")
        print(f"🔶 BNB:  {futures_bnb:.6f}")

        # Check Open Positions
        positions = futures_exchange.fetch_positions()
        active_positions = [p for p in positions if float(p['contracts']) > 0]
        
        pnl_unrealized = 0
        if active_positions:
            print(colored(f"\n[ACTIVE POSITIONS: {len(active_positions)}]", "green"))
            for p in active_positions:
                symbol = p['symbol']
                side = p['side']
                amt = p['contracts']
                entry = p['entryPrice']
                upnl = p['unrealizedPnl']
                pnl_unrealized += float(upnl)
                print(f"  • {symbol} {side.upper()} x{amt} @ ${entry} (uPnL: ${upnl})")
        else:
            print(colored("\n[NO ACTIVE POSITIONS]", "white"))

    except Exception as e:
        print(colored(f"❌ Error fetching FUTURES balance: {str(e)}", "red"))
        futures_usdt = 0
        pnl_unrealized = 0

    # 3. Total Aggregation
    # Get current BNB Price for conversion
    try:
        ticker = spot_exchange.fetch_ticker('BNB/USDT')
        bnb_price = ticker['last']
    except:
        bnb_price = 0

    total_bnb_val = (spot_bnb + futures_bnb) * bnb_price
    total_equity = spot_usdt + futures_usdt + total_bnb_val + pnl_unrealized
    
    print(colored("\n" + "="*40, "white"))
    print(colored(f"📊 TOTAL REAL EQUITY: ${total_equity:.2f}", "white", attrs=['bold']))
    print(colored("="*40, "white"))

    # 4. Verdict
    STARTING_CAPITAL = 10.0 # From memory
    if total_equity < STARTING_CAPITAL * 0.5:
        print(colored("💀 CRITICAL DRAWDOWN DETECTED (>50% LOSS)", "red", attrs=['bold', 'blink']))
        print(colored("RECOMMENDATION: INITIATE EMERGENCY PROTOCOL", "red"))
    elif total_equity < STARTING_CAPITAL:
        print(colored(f"📉 DRAWDOWN: -{((STARTING_CAPITAL - total_equity)/STARTING_CAPITAL)*100:.1f}%", "yellow"))
    else:
        print(colored(f"📈 PROFIT: +{((total_equity - STARTING_CAPITAL)/STARTING_CAPITAL)*100:.1f}%", "green"))

if __name__ == "__main__":
    audit_pnl()
