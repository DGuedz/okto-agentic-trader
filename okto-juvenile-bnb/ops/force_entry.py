import sys
import os
from termcolor import colored

# Ensure core modules are importable
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ops.scalp_rsi import ScalpTentacle

def force_entry():
    print(colored("\n🚨 OKTO MANUAL OVERRIDE: FORCING ENTRY", "red", attrs=['bold', 'blink']))
    print("-" * 50)
    
    bot = ScalpTentacle()
    
    # Force buy execution regardless of RSI
    print(colored("[SYSTEM] BYPASSING RSI CHECKS...", "yellow"))
    print(colored("[EXEC] INITIATING MARKET BUY ORDER...", "cyan"))
    
    # Execute a small test trade (default logic in execute_buy handles size)
    # We might want to pass a small specific amount if possible, but execute_buy calculates based on balance.
    # Let's trust the risk management in execute_buy (95% of free margin, which is ~$13).
    
    bot.execute_buy()

if __name__ == "__main__":
    force_entry()
