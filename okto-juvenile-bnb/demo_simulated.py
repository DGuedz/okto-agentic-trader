import time
import random

def simulate_growth(initial_capital, target_profit, leverage, trades_per_day):
    capital = initial_capital
    profit_accumulated = 0.0
    win_rate = 0.65  # Conservador para scalp
    avg_win = 0.004  # 0.4% por trade (com alavancagem 5x = 2% ROE)
    avg_loss = 0.002 # 0.2% stop loss curto
    
    print(f"\n🚀 SIMULAÇÃO DE SCALP: ${initial_capital:.2f} -> +${target_profit:.2f}")
    print(f"⚙️  Config: {leverage}x Leverage | {trades_per_day} trades/dia")
    print("-" * 50)
    
    days = 0
    while profit_accumulated < target_profit:
        days += 1
        daily_pnl = 0
        
        print(f"\n📅 DIA {days}:")
        for i in range(trades_per_day):
            is_win = random.random() < win_rate
            trade_size = capital * 0.95 # Usa 95% do capital livre
            
            if is_win:
                pnl = trade_size * avg_win * leverage
                result = "✅ WIN "
            else:
                pnl = -trade_size * avg_loss * leverage
                result = "❌ LOSS"
                
            daily_pnl += pnl
            profit_accumulated += pnl
            
            # Simula composição ou saque parcial (aqui mantemos fixo pra simplificar meta)
            # capital += pnl 
            
            print(f"   Trade {i+1}: {result} | PnL: ${pnl:.4f}")
            
            if profit_accumulated >= target_profit:
                break
                
        print(f"   💰 Saldo do Dia: ${daily_pnl:.4f} | Total Acumulado: ${profit_accumulated:.4f}")
        
        if days > 30: # Safety break
            print("\n⚠️ Meta não atingida em 30 dias (ajustar estratégia).")
            break
            
    print("-" * 50)
    print(f"🏁 RESULTADO FINAL:")
    print(f"   Tempo necessário: {days} dias")
    print(f"   Lucro Total: ${profit_accumulated:.2f}")
    print(f"   Novo Saldo: ${initial_capital + profit_accumulated:.2f}")

# Cenário 1: Conservador (3 trades/dia, 5x)
simulate_growth(11.21, 3.79, 5, 3) # Meta: Chegar a $15 (+$3.79)
