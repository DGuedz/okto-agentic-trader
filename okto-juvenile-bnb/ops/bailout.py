import ccxt
import os
import sys
import time
from termcolor import colored
from dotenv import load_dotenv

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ops.obi_analyzer import analyze_obi

def emergency_bailout():
    """
    EMERGENCY PROTOCOL:
    Analyzes OBI and PnL. If situation is critical, force closes position.
    """
    load_dotenv("config/.env")
    
    api_key = os.getenv("BINANCE_API_KEY")
    secret = os.getenv("BINANCE_SECRET")
    
    if not api_key or not secret:
        print(colored("❌ Missing Keys", "red"))
        return

    try:
        exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret,
            'enableRateLimit': True,
            'options': {'defaultType': 'future'}
        })
        
        # 1. Check Positions
        positions = exchange.fetch_positions()
        active = [p for p in positions if float(p['contracts']) > 0]
        
        if not active:
            print(colored("✅ NO ACTIVE POSITIONS. YOU ARE SAFE.", "green"))
            return

        for p in active:
            symbol = p['symbol']
            amt = float(p['contracts'])
            side = p['side']
            entry = float(p['entryPrice'])
            pnl = float(p['unrealizedPnl'])
            
            print(colored(f"\n🚨 ACTIVE THREAT: {symbol} {side.upper()} x{amt} (PnL: ${pnl:.2f})", "yellow", attrs=['bold']))
            
            # 2. Analyze OBI (The Judge)
            print("🔍 ANALYZING LIQUIDITY FLOW (OBI)...")
            obi_data = analyze_obi(symbol)
            
            should_bail = False
            reason = ""
            
            if obi_data:
                obi = obi_data['obi']
                
                # RULE 1: OBI FLIP
                # If Long and OBI turns Negative (Sell Pressure), BAIL.
                if side == 'long' and obi < -0.05:
                    should_bail = True
                    reason = f"OBI FLIPPED NEGATIVE ({obi:.4f})"
                
                # RULE 2: STOP LOSS HIT
                # Hard Stop at -$3.00 (30% of account)
                if pnl < -3.0:
                    should_bail = True
                    reason = "HARD STOP LOSS HIT (-$3.00)"
                    
                # RULE 3: BREAK-EVEN EXIT (STRATEGIC RESET)
                # Exit if PnL is effectively zero (covers fees) to reset strategy
                if pnl > 0.05:
                    should_bail = True
                    reason = "BREAK-EVEN TARGET REACHED (RESET)"

            if should_bail:
                print(colored(f"💀 BAILOUT TRIGGERED: {reason}", "red", attrs=['bold', 'blink']))
                print("⏳ EXECUTING EMERGENCY CLOSE IN 3s... (CTRL+C TO ABORT)")
                time.sleep(3)
                
                # CLOSE IT
                if side == 'long':
                    exchange.create_market_sell_order(symbol, amt)
                else:
                    exchange.create_market_buy_order(symbol, amt)
                    
                print(colored("✅ POSITION CLOSED. STRATEGY RESET.", "green"))
                return True # Signal exit
            else:
                print(colored("🛡️ HOLDING LINE: OBI IS STABLE (> -0.05).", "cyan"))
                print(f"   Current OBI: {obi_data['obi']:.4f}")
                return False

    except Exception as e:
        print(colored(f"❌ BAILOUT FAILED: {str(e)}", "red"))
        return False

if __name__ == "__main__":
    print(colored("🔭 STARTING CONTINUOUS MONITORING LOOP (CTRL+C TO STOP)", "magenta", attrs=['bold']))
    while True:
        try:
            exited = emergency_bailout()
            if exited:
                print("🏁 MISSION COMPLETE: POSITION EXITED.")
                break
            
            # Rate Limit Friendly Wait
            time.sleep(10)
            print("." * 20)
            
        except KeyboardInterrupt:
            print("\n🛑 MONITORING STOPPED BY USER")
            break
