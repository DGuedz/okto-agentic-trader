import json
import time
import random
import os

# Simulação de Monitoramento (Stub para demonstração)
def monitor_trade(plan_file):
    print("🛰️  MONITORING ACTIVE (20x Scalp Mode)")
    print("-" * 40)
    
    with open(plan_file, 'r') as f:
        plan = json.load(f)
        
    if plan.get('action') == 'NO_TRADE':
        print(f"⏸️  SKIP: {plan.get('reason', 'No setup')}")
        return

    entry = plan['params']['entry']
    sl = plan['params']['sl']
    tp1 = plan['params']['tp1']
    
    side = plan['params'].get('side', 'BUY')
    
    print(f"🎯 TARGETS ({side}): Entry ${entry} | SL ${sl} | TP1 ${tp1}")
    print("⏳ Waiting for fill...")
    time.sleep(1)
    print("✅ FILLED at Market")
    
    # Simula movimento de preço
    current_price = entry
    pnl_pct = 0.0
    
    # Loop de 5 steps simulados
    for i in range(5):
        noise = random.uniform(-0.1, 0.2) if side == 'BUY' else random.uniform(-0.2, 0.1)
        current_price += noise
        
        if side == 'BUY':
            pnl_pct = ((current_price - entry) / entry) * 20 * 100
        else:
            pnl_pct = ((entry - current_price) / entry) * 20 * 100
        
        print(f"   Tick {i+1}: ${current_price:.2f} (PnL: {pnl_pct:.2f}%)")
        
        # Lógica de Gestão
        if pnl_pct >= 4.0:
            print("🛡️  Anti-Liquidation Triggered: SL moved to Break-Even (+0.5%)")
            break
        elif (side == 'BUY' and current_price <= sl) or (side == 'SELL' and current_price >= sl):
            print("❌ STOP LOSS HIT")
            break
        elif (side == 'BUY' and current_price >= tp1) or (side == 'SELL' and current_price <= tp1):
            print("💰 TP1 HIT: Taking 40% profit")
            break
            
        time.sleep(0.5)

    print("-" * 40)
    print("🏁 TRADE CYCLE COMPLETE")

if __name__ == "__main__":
    # Cria plan.json dummy se não existir
    if not os.path.exists("plan.json"):
        with open("plan.json", "w") as f:
            json.dump({"params": {"entry": 618.6, "sl": 617.78, "tp1": 619.14}}, f)
            
    monitor_trade("plan.json")
