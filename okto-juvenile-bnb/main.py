import sys
import os
from termcolor import colored

# Ensure core modules are importable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.safety import check_network_health
from core.connector import connect_vault
from ops.scalp_rsi import ScalpTentacle

def main():
    # 1. Safety Check (Silent Mode)
    is_safe, safety_details = check_network_health(silent=True)
    
    # 2. Vault Connection
    vault_status = connect_vault()
    
    # 3. Market Scan (Tentacle 01)
    scalper = ScalpTentacle()
    market_data = scalper.scan_market()
    
    # Formatting constants
    LABEL_WIDTH = 40
    
    print("\n" + "="*60)
    
    # SYSTEM STATUS
    print(f"{'[SYSTEM] OKTO AGENTIC ASSISTANT':.<{LABEL_WIDTH}} " + 
          colored("ONLINE", "green", attrs=['bold']))

    
    # NET STATUS
    net_status = "STABLE" if safety_details["connected"] else "DOWN"
    net_color = "green" if safety_details["connected"] else "red"
    print(f"{'[NET] BNB CHAIN CONNECTION':.<{LABEL_WIDTH}} " + 
          colored(net_status, net_color, attrs=['bold']))
          
    # RPC PROVIDER INFO
    print(f"{'[LINK] PROVIDER TYPE':.<{LABEL_WIDTH}} " + 
          colored(safety_details['provider'], "cyan", attrs=['bold']))
          
    latency_color = "green" if safety_details['latency_ms'] < 200 else "yellow"
    print(f"{'[PING] NETWORK LATENCY':.<{LABEL_WIDTH}} " + 
          colored(f"{safety_details['latency_ms']:.1f}ms", latency_color, attrs=['bold']))
    
    if safety_details['latency_ms'] < 200 and "Alchemy" in safety_details['provider']:
         print(f"{'[SPEED] HIGH FREQUENCY LINK':.<{LABEL_WIDTH}} " + 
          colored("ESTABLISHED", "yellow", attrs=['bold']))

    # GAS STATUS
    gas_status = "OPTIMAL" if is_safe else "HIGH COST"
    gas_color = "green" if is_safe else "yellow"
    print(f"{'[GAS] COST EFFICIENCY':.<{LABEL_WIDTH}} " + 
          colored(gas_status, gas_color, attrs=['bold']))

          
    # MODE STATUS
    print(f"{'[MODE] AUTONOMOUS TREASURY':.<{LABEL_WIDTH}} " + 
          colored("ACTIVE", "cyan", attrs=['bold']))

    # VAULT STATUS
    if vault_status["status"]:
        addr_short = f"{vault_status['address'][:6]}...{vault_status['address'][-4:]}"
        print(f"{'[VAULT] ADDRESS IDENTIFIED':.<{LABEL_WIDTH}} " + 
              colored(addr_short, "blue", attrs=['bold']))
        
        balance_fmt = f"{vault_status['balance_bnb']:.4f} BNB"
        # Color code liquidity
        liq_color = "red" if vault_status['balance_bnb'] == 0 else "yellow" if vault_status['balance_bnb'] < 0.01 else "green"
        
        print(f"{'[TREASURY] LIQUIDITY POOL':.<{LABEL_WIDTH}} " + 
              colored(balance_fmt, liq_color, attrs=['bold']))
    else:
        print(f"{'[VAULT] CONNECTION STATUS':.<{LABEL_WIDTH}} " + 
              colored(f"FAILED ({vault_status['msg']})", "red", attrs=['bold']))

    # MARKET SCAN
    print("-" * 60)
    if market_data["success"]:
        print(f"{'[SCAN] BNB/USDT PRICE':.<{LABEL_WIDTH}} " + 
              colored(f"${market_data['price']:.2f}", "white", attrs=['bold']))
              
        rsi_val = market_data['rsi']
        rsi_color = "green" if rsi_val < 30 else "red" if rsi_val > 70 else "white"
        print(f"{'[INDICATOR] RSI (14)':.<{LABEL_WIDTH}} " + 
              colored(f"{rsi_val:.2f}", rsi_color, attrs=['bold']))
        
        if rsi_val < 30:
             print(f"{'[DECISION] AI SIGNAL':.<{LABEL_WIDTH}} " + 
              colored("BUY OPPORTUNITY DETECTED", "green", attrs=['bold']))
        else:
             print(f"{'[DECISION] AI SIGNAL':.<{LABEL_WIDTH}} " + 
              colored("WAITING FOR DIP", "white"))

    else:
         print(f"{'[SCAN] MARKET DATA':.<{LABEL_WIDTH}} " + 
              colored("UNAVAILABLE", "red"))

    print("="*60 + "\n")

    if not is_safe:
        print(colored("🔴 CRITICAL: Safety protocols triggered halt.", "red"))
        sys.exit(1)
        
    if not vault_status["status"]:
        print(colored("⚠️  WARNING: Vault not connected. Operating in OBSERVATION ONLY mode.", "yellow"))

if __name__ == "__main__":
    main()
