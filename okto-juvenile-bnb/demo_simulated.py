#!/usr/bin/env python3
"""
DEMO SIMULADA - Para vídeo de demonstração
Simula uma operação completa sem usar API real
"""

import time
import random
from termcolor import colored

def simulated_demo():
    print("🎬 INICIANDO DEMO SIMULADA PARA VÍDEO")
    print("=" * 55)
    print("📱 CONECTANDO À BINANCE FUTURES...")
    time.sleep(1)
    
    # Simular análise de mercado
    print("\n📊 ANALISANDO MERCADO BNB/USDT")
    time.sleep(1)
    
    current_price = 630.50 + random.uniform(-2, 2)
    print(f"   • Preço Atual: ${current_price:.2f}")
    print(f"   • RSI: {random.randint(45, 65)}")
    print(f"   • Volume: {random.randint(1000, 5000)} BNB")
    print(f"   • Tendência: ALTA 🐂")
    
    time.sleep(1)
    print("\n🎯 IDENTIFICANDO OPORTUNIDADE DE ENTRADA")
    print("   • OBI: Pressão compradora forte")
    print("   • Bollinger: Preço próximo à banda inferior")
    print("   • Setup: HIGH PROBABILITY")
    
    time.sleep(1)
    print("\n🚀 EXECUTANDO ORDEM DE COMPRA")
    print("   • Tipo: MARKET BUY")
    print("   • Par: BNB/USDT")
    print("   • Tamanho: 0.05 BNB")
    print("   • Alavancagem: 5x")
    
    # Simular execução
    for i in range(3):
        print(f"   • Processando{'.' * (i+1)}")
        time.sleep(0.5)
    
    entry_price = current_price + random.uniform(0.1, 0.5)
    print(colored(f"\n✅ ORDEM EXECUTADA - ENTRY: ${entry_price:.2f}", 'green'))
    print(f"   • Custo: ${entry_price * 0.05:.2f} USDT")
    print(f"   • Posição: LONG BNB")
    
    time.sleep(2)
    print("\n📈 MONITORANDO POSIÇÃO...")
    
    # Simular movimento de preço
    for i in range(5):
        price_move = entry_price + random.uniform(1, 3)
        pnl = (price_move - entry_price) * 0.05 * 5  # 5x leverage
        print(f"   • Preço: ${price_move:.2f} | PnL: ${pnl:.2f}")
        time.sleep(1)
    
    # Simular fechamento
    exit_price = entry_price + random.uniform(2, 4)
    final_pnl = (exit_price - entry_price) * 0.05 * 5
    
    print(f"\n🎯 ATINGINDO TARGET...")
    time.sleep(1)
    print(colored(f"✅ FECHANDO POSIÇÃO - EXIT: ${exit_price:.2f}", 'green'))
    print(colored(f"💰 LUCRO: ${final_pnl:.2f} USDT", 'green', attrs=['bold']))
    
    print(f"\n📊 ESTATÍSTICAS DA OPERAÇÃO:")
    print(f"   • Entry: ${entry_price:.2f}")
    print(f"   • Exit: ${exit_price:.2f}")
    print(f"   • Movimento: +{(exit_price - entry_price):.2f} ({((exit_price - entry_price)/entry_price*100):.2f}%)")
    print(f"   • PnL: ${final_pnl:.2f} USDT")
    print(f"   • ROI: {(final_pnl/(entry_price*0.05)*100):.1f}%")
    
    time.sleep(1)
    print("\n🎬 DEMO SIMULADA CONCLUÍDA - PRONTO PARA GRAVAÇÃO!")
    print("💡 Use este vídeo para demonstrar a lógica de execução do Okto")

if __name__ == "__main__":
    simulated_demo()