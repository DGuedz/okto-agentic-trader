import json
import time
import random
import argparse
import sys

def run_grid(symbol, lower, upper, grids, capital=11.21, fee_tier=0.0002):
    print(f"🕸️  GRID LOOP: {symbol} | ${lower} - ${upper} | {grids} Grids")
    print(f"💰 Capital: ${capital:.2f} | Mode: Maker (Limit Orders)")
    
    # Kill-Switch Buffers (0.25%)
    kill_upper = upper * 1.0025
    kill_lower = lower * 0.9975
    print(f"🛡️  Kill-Switch: < ${kill_lower:.2f} or > ${kill_upper:.2f}")
    
    # Anti-Trend Counters
    consecutive_buys = 0
    consecutive_sells = 0
    max_consecutive = 3
    
    # Validação de Step Mínimo (Fee Protection)
    step = (upper - lower) / grids
    step_pct = (step / lower) * 100
    min_step_pct = fee_tier * 2 * 100 * 1.5 # 2x Fee + 50% buffer
    
    print(f"📏 Step Size: ${step:.4f} ({step_pct:.3f}%)")
    
    if step_pct < min_step_pct:
        print(f"⚠️  ALERTA CRÍTICO: Step {step_pct:.3f}% < Mínimo Lucrativo {min_step_pct:.3f}%")
        print("   -> Aumente o range ou diminua o número de grids.")
        recommended_grids = int((upper - lower) / (lower * (min_step_pct/100)))
        print(f"   -> Sugestão: Max {recommended_grids} grids para este range.")
        return

    # Validação de Min Notional (Binance geralmente $5 USDT)
    notional_per_grid = (capital * 20) / grids # Usando 20x leverage
    print(f"💵 Notional por Grid (20x): ${notional_per_grid:.2f}")
    
    if notional_per_grid < 5.0:
        print("⚠️  ALERTA CRÍTICO: Notional < $5.0 (Binance Minimum)")
        print("   -> Aumente o capital ou a alavancagem.")
        return

    # Gera níveis do Grid
    levels = [round(lower + i * step, 2) for i in range(grids + 1)]
    print(f"📊 Levels: {levels}")
    
    # Simula preço atual (no meio do range)
    current_price = (upper + lower) / 2
    
    # Determina ordens iniciais (Simétrico: Metade Buy, Metade Sell)
    mid_index = len(levels) // 2
    buy_orders = {l for l in levels[:mid_index]}
    sell_orders = {l for l in levels[mid_index+1:]}
    
    print("-" * 50)
    print(f"🟢 BUY LIMITS: {sorted(list(buy_orders))}")
    print(f"�� SELL LIMITS: {sorted(list(sell_orders))}")
    print("-" * 50)
    
    # Loop de Simulação (10 ticks)
    total_pnl = 0.0
    
    for i in range(10):
        # Simula volatilidade dentro do range
        noise = random.uniform(-step*0.8, step*0.8)
        current_price += noise
        
        # Kill-Switch Check
        if current_price < kill_lower or current_price > kill_upper:
            print(f"🚨 KILL-SWITCH TRIGGERED: Price ${current_price:.2f} out of bounds!")
            break
            
        # Mantém dentro do range visual do print (Bollinger)
        current_price = max(lower, min(upper, current_price))
        
        print(f"Tick {i+1}: ${current_price:.2f}", end=" ")
        
        executed = False
        
        # Check Buys
        # Lógica One-Order-Per-Level: Só executa se a ordem existe no set
        potential_fills = [l for l in buy_orders if current_price <= l]
        
        if potential_fills:
            # Anti-Trend Protection
            if consecutive_buys >= max_consecutive:
                print(f"⚠️  ANTI-TREND: Pausing BUYs (3 consecutive)", end="")
            else:
                filled = max(potential_fills) # Pega o mais alto que foi atingido
                buy_orders.remove(filled)
                
                # Reposiciona Venda acima
                new_sell = round(filled + step, 2)
                if new_sell <= upper and new_sell not in sell_orders:
                    sell_orders.add(new_sell)
                    print(f"✅ BUY @ ${filled} -> New SELL @ ${new_sell}", end="")
                    consecutive_buys += 1
                    consecutive_sells = 0
                    executed = True
                
        # Check Sells
        potential_fills = [l for l in sell_orders if current_price >= l]
        
        if potential_fills:
            # Anti-Trend Protection
            if consecutive_sells >= max_consecutive:
                print(f"⚠️  ANTI-TREND: Pausing SELLs (3 consecutive)", end="")
            else:
                filled = min(potential_fills) # Pega o mais baixo que foi atingido
                sell_orders.remove(filled)
                
                # Reposiciona Compra abaixo
                new_buy = round(filled - step, 2)
                if new_buy >= lower and new_buy not in buy_orders:
                    buy_orders.add(new_buy)
                    
                    # Cálculo de PnL Bruto (Step)
                    gross_profit = step
                    # Fee Estimada (0.04% taker na saída simulada ou 0.02% maker)
                    fees = (filled * 0.0004)
                    net_profit = gross_profit - fees
                    total_pnl += net_profit
                    
                    print(f"✅ SELL @ ${filled} -> New BUY @ ${new_buy} (PnL: +${net_profit:.4f})", end="")
                    consecutive_sells += 1
                    consecutive_buys = 0
                    executed = True
            
        if not executed:
            print("(No Fill)", end="")
            
        print("")
        time.sleep(0.5)

    print("-" * 50)
    print(f"🏁 SIMULAÇÃO FINALIZADA")
    print(f"💰 PnL Estimado: ${total_pnl:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", default="BNB/USDT")
    parser.add_argument("--lower", type=float, default=617.55)
    parser.add_argument("--upper", type=float, default=619.45)
    parser.add_argument("--grids", type=int, default=4) # Reduzido para 4 para garantir step > fee
    args = parser.parse_args()
    
    run_grid(args.symbol, args.lower, args.upper, args.grids)
