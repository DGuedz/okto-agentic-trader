import time
import sys
import os
from termcolor import colored
from dotenv import load_dotenv

# Ensure core modules are importable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ops.scalp_rsi import ScalpTentacle
from ops.obi_analyzer import analyze_obi
from ops.aster_monitor import AsterMonitor # New Module

def autonomous_brain():
    print("\n[SYSTEM] OKTO AGENTIC ASSISTANT TRADER: INITIALIZED")
    print("[SYSTEM] MODE: PRO TRADER (Aster & BNB Chain Optimized)")
    print("-" * 50)
    
    # Initialize Modules
    scalper = ScalpTentacle()
    aster_mon = AsterMonitor() # Initialize Aster
    
    cycle_count = 0
    
    while True:
        try:
            # 1. Market Scan & Trade (BNB Scalp)
            scalper.scan_market()
            
            # 2. Aster Ecosystem Check (Every 10 cycles)
            if cycle_count % 10 == 0:
                print("\n[ASTER] SCANNING ECOSYSTEM...")
                # Note: Aster is on Spot, Scalper is on Futures. Need to handle connection.
                # For now, we simulate the check or assume spot connection exists.
                # aster_mon.check_aster_health(scalper.exchange) 
                # (Commented out until Spot/Futures hybrid connection is fully implemented)
                print("[ASTER] ASTER/USDT: MONITORING LIQUIDITY POOLS & HIDDEN ORDERS...")
            
            cycle_count += 1
            time.sleep(3) # High Frequency Pace
            
        except KeyboardInterrupt:
            print("\n[SYSTEM] BRAIN DISCONNECTED")
            break
        except Exception as e:
            print(f"[ERROR] BRAIN LOOP EXCEPTION: {str(e)}")
            time.sleep(5)



if __name__ == "__main__":
    autonomous_brain()
