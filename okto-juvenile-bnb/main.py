import sys
import os
import time
import builtins
from termcolor import colored
from core.sanitizer import LogSanitizer
from core.mind_shield import MindShield

# --- SILENT FORTRESS: LOG SANITIZATION ---
# Override print globally to mask sensitive data
original_print = builtins.print
def secure_print(*args, **kwargs):
    kwargs['flush'] = True # Force flush for real-time monitoring
    sanitized_args = [LogSanitizer.clean(str(arg)) for arg in args]
    original_print(*sanitized_args, **kwargs)
builtins.print = secure_print
# -----------------------------------------

# Ensure core modules are importable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.safety import check_network_health
from core.connector import connect_vault
from ops.scalp_rsi import ScalpTentacle
from ops.mission_control import MissionControl
from src.safety_rails import SafetyRails
from ops.aster_farmer import AsterFarmer

def main():
    # Initialize Mission Control & Safety Rails & Aster Farmer
    mission = MissionControl()
    rails = SafetyRails(spec_path='specs/genesis.yaml')
    farmer = AsterFarmer()
    
    loop_count = 0

    # 1. Safety Check (Silent Mode)
    is_safe, safety_details = check_network_health(silent=True)
    
    # 2. Vault Connection
    vault_status = connect_vault()
    
    # 3. Market Scan (Tentacle 01)
    scalper = ScalpTentacle()
    
    while True:
        try:
            # 0. MISSION STATUS CHECK (BOOTSTRAP)
            # Fetch equity (simulated for now based on USDT balance + position)
            # In a real loop, we would track PnL more accurately.
            # Here we assume we can check balance via scalper instance
            balance = scalper.exchange.fetch_balance()
            total_equity = balance['USDT']['total'] # Approximate
            
            # 0.1 VSC SAFETY RAILS CHECK (GAS & NETWORK)
            if not rails.check_gas():
                print(colored("🛑 CRITICAL STOP: NETWORK GAS TOO HIGH. PAUSING OPERATIONS.", "red", attrs=['bold']))
                time.sleep(60) # Wait 1 min before retry
                continue

            mission_status = mission.analyze_status(total_equity)
            mission.print_hud(total_equity)
            
            if mission_status['health'] == 'CRITICAL':
                print(colored("🛑 CRITICAL STOP: DUST RISK LIMIT REACHED. PRESERVING CAPITAL.", "red", attrs=['bold']))
                sys.exit(0)

            # Pass Mission Phase to Scalper for Strategy Adjustment
            current_phase = mission_status['phase']
            
            market_data = scalper.scan_market(phase=current_phase)
            
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
                  colored(f"ACTIVE ({current_phase})", "cyan", attrs=['bold']))

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
                # Unpack Data
                price = market_data['price']
                rsi_val = market_data['rsi']
                atr_val = market_data['atr']
                bb = market_data['bb']
                vwap_val = market_data['vwap']
                funding_val = market_data['funding']
                delta_val = market_data['delta']
                
                # Display Prices
                print(f"{'[SCAN] BNB/USDT PRICE':.<{LABEL_WIDTH}} " + 
                      colored(f"${market_data['price']:.2f}", "white", attrs=['bold']))
                
                # RSI Display
                rsi_color = "green" if rsi_val < 30 else "red" if rsi_val > 70 else "white"
                print(f"{'[INDICATOR] RSI (14)':.<{LABEL_WIDTH}} " + 
                      colored(f"{rsi_val:.2f}", rsi_color, attrs=['bold']))
                      
                # BB Display
                bb_pos = "INSIDE"
                bb_color = "white"
                if price <= bb['lower']: 
                    bb_pos = "LOWER BAND TOUCH"
                    bb_color = "green"
                elif price >= bb['upper']:
                    bb_pos = "UPPER BAND TOUCH"
                    bb_color = "red"
                    
                print(f"{'[INDICATOR] BOLLINGER':.<{LABEL_WIDTH}} " + 
                      colored(bb_pos, bb_color))

                # VWAP Display
                vwap_status = "ABOVE (BULL)" if price > vwap_val else "BELOW (BEAR)"
                vwap_color = "green" if price > vwap_val else "red"
                print(f"{'[INDICATOR] VWAP TREND':.<{LABEL_WIDTH}} " + 
                      colored(vwap_status, vwap_color))
                      
                # Delta Display
                delta_status = "AGGRESSIVE BUYING" if delta_val > 0 else "AGGRESSIVE SELLING"
                delta_color = "green" if delta_val > 0 else "red"
                print(f"{'[INDICATOR] VOLUME DELTA':.<{LABEL_WIDTH}} " + 
                      colored(delta_status, delta_color))

                # Funding Display
                fund_color = "red" if abs(funding_val) > 0.01 else "white"
                print(f"{'[DATA] FUNDING RATE':.<{LABEL_WIDTH}} " + 
                      colored(f"{funding_val*100:.4f}%", fund_color))

                # SMART GRID LOGIC (AUTO-TRAP)
                print("="*60)
                print(colored(f"🕸️  ACTIVATING SMART GRID SYSTEM [{current_phase}]...", "cyan"))
                
                # 1. Clear old traps (stale orders)
                scalper.cancel_all_open_orders()
                
                # 2. Set new traps
                # Check if we already have a position
                # For simplicity in this demo, we assume we want to enter or re-enter
                # Real logic would check `exchange.fetch_positions()` first
                
                # Pass Phase to setup_smart_grid to adjust aggressiveness
                scalper.setup_smart_grid(phase=current_phase)
                
            else:
                 print(f"{'[SCAN] MARKET DATA':.<{LABEL_WIDTH}} " + 
                      colored("UNAVAILABLE", "red"))

            print("="*60 + "\n")

            if not is_safe:
                print(colored("🔴 CRITICAL: Safety protocols triggered halt.", "red"))
                sys.exit(1)
                
            if not vault_status["status"]:
                print(colored("⚠️  WARNING: Vault not connected. Operating in OBSERVATION ONLY mode.", "yellow"))
            
            # --- [OKTO-ECON-01] YIELD FARMING & BRIDGING ---
            loop_count += 1
            
            # 1. Harvest Simulation (Every 5 ticks)
            if loop_count % 5 == 0:
                farmed = farmer.harvest() # Returns float
                if farmed:
                    mission.update_yield(farmed)
                    print(colored(f"🌾 [ASTER] HARVESTED: {farmed:.4f} ASTER | TOTAL: {mission.total_yield_farmed:.4f}", "green", attrs=['bold']))

            # 2. Profit Bridging (Every 3 ticks - Simulation)
            if loop_count % 3 == 0:
                simulated_profit = 2.50
                mission.add_profit(simulated_profit)
                print(colored(f"💰 [SCALPER] PROFIT CAPTURED: +${simulated_profit:.2f} | POOL: ${mission.unallocated_profit:.2f}", "cyan"))

            # 3. Auto-Deposit to Vault
            if mission.unallocated_profit >= 10.0:
                # MIND SHIELD CHECK
                if MindShield.validate_intent("WITHDRAW", {"destination": "ASTER_VAULT", "amount": mission.unallocated_profit}):
                    print(colored(f"🌉 [BRIDGE] MOVING PROFIT (${mission.unallocated_profit:.2f}) TO ASTER VAULT...", "magenta", attrs=['bold']))
                    if farmer.deposit_profits(mission.unallocated_profit):
                        mission.reset_profit()
                else:
                    print(colored("🛑 [MIND SHIELD] BRIDGE BLOCKED BY SECURITY PROTOCOL", "red"))
            # -----------------------------------------------

            print("=" * 60)
            print(colored("⏳ WAITING NEXT TICK (30s)...", "yellow"))
            time.sleep(30)

        except KeyboardInterrupt:
            print("\n[SYSTEM] SHUTDOWN REQUESTED. BYE.")
            sys.exit(0)
        except Exception as e:
            print(f"[ERROR] MAIN LOOP: {str(e)}")
            time.sleep(5)

if __name__ == "__main__":
    main()
