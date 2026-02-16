import time
import sys
import random
from termcolor import colored

def type_writer(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def okto_header():
    print(colored("\n" + "="*60, "magenta"))
    print(colored("   🐙 OKTO AGENTIC ASSISTANT v1.1 [HEADLESS MODE]", "magenta", attrs=['bold']))
    print(colored("   Status: ONLINE | Network: BSC | Vault: CONNECTED", "green"))
    print(colored("="*60 + "\n", "magenta"))

def sequence_boot():
    okto_header()
    time.sleep(1)
    print("[INIT] Loading specs/genesis.yaml...", end=" "); time.sleep(0.5); print(colored("OK", "green"))
    print("[INIT] Connecting to Safety Rails...", end=" "); time.sleep(0.5); print(colored("CONNECTED (ChainID: 56)", "green"))
    print("[INIT] Checking Gas Prices...", end=" "); time.sleep(0.3); print(colored("OPTIMAL (0.05 Gwei)", "green"))
    print(colored("[SYSTEM] Silent Fortress Protocol: ACTIVE", "cyan"))
    print(colored("[SYSTEM] Mind Shield: ARMED", "cyan"))
    print("-" * 60)

def sequence_scalp():
    print(colored("\n[MONITOR] DETECTING IDLE COMPUTE RESOURCES...", "blue"))
    time.sleep(1.5)
    print(colored(">> IDLE STATE CONFIRMED. INITIATING SCALP SEQUENCE.", "yellow", attrs=['bold']))
    
    print("[SCAN] Scanning BNB/USDT...", end=" "); time.sleep(0.5); print(colored("OPPORTUNITY FOUND (RSI: 28)", "green"))
    
    type_writer("[EXEC] PLACING BUY ORDER | LIMIT @ $635.20 | SIZE: 0.5 BNB", speed=0.03)
    time.sleep(1)
    print(colored("✅ ORDER FILLED: 0x8a7...3b2", "green"))
    
    time.sleep(2)
    print("[MARKET] Price Update: $635.50...", end="\r"); time.sleep(0.5)
    print("[MARKET] Price Update: $636.10...", end="\r"); time.sleep(0.5)
    print("[MARKET] Price Update: $637.80   ", end="\n")
    
    print(colored("🎯 TARGET HIT. CLOSING POSITION.", "cyan"))
    print(colored("💰 [SCALPER] PROFIT CAPTURED: +$4.20 (Unallocated: $12.50)", "green", attrs=['bold']))

def sequence_bridge():
    print(colored("\n[BRIDGE] UNALLOCATED PROFIT THRESHOLD REACHED ($10.00)", "magenta"))
    time.sleep(1)
    
    print("[MIND SHIELD] Validating Intent...", end=" "); time.sleep(0.5); print(colored("AUTHORIZED (Dest: ASTER_VAULT)", "green"))
    
    type_writer("🌉 BRIDGING $12.50 TO ASTER YIELD VAULT...", speed=0.03)
    time.sleep(2)
    print(colored("✅ TX CONFIRMED: 0x9c2...8f1 | GAS: 0.0002 BNB", "green"))

def sequence_farm():
    print(colored("\n[ASTER] DEPOSITING TO PERPETUAL VAULT...", "magenta"))
    time.sleep(1)
    print(colored("🌾 [FARM] STAKING COMPLETE. APY: 18.5%", "green"))
    print(colored("📈 [OKTO] TOTAL YIELD FARMED: 0.05 ASTER", "green", attrs=['bold']))
    
    print("\n" + "="*60)
    print(colored("   STATUS: FARMING | NEXT CYCLE: 30s", "yellow"))
    print(colored("="*60 + "\n", "magenta"))

if __name__ == "__main__":
    try:
        sequence_boot()
        time.sleep(1)
        sequence_scalp()
        time.sleep(1)
        sequence_bridge()
        time.sleep(1)
        sequence_farm()
    except KeyboardInterrupt:
        print("\n[STOP] Preview terminated.")