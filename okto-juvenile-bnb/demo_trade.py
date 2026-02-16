#!/usr/bin/env python3
"""
DEMO TRADE SCRIPT - Para vídeo de demonstração
Abre uma operação de 0.01 BNB (tamanho mínimo) na Binance
"""

import os
import sys
import time
from termcolor import colored

# Adicionar o diretório ops ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'ops'))

from scalp_rsi import ScalpTentacle

def demo_trade():
    print("🎬 INICIANDO DEMO TRADE PARA VÍDEO")
    print("=" * 50)
    
    # Inicializar o scalper
    scalper = ScalpTentacle()
    
    try:
        # 1. Obter preço atual do BNB
        ticker = scalper.exchange.fetch_ticker('BNB/USDT:USDT')
        current_price = ticker['last']
        print(f"📊 PREÇO ATUAL BNB: ${current_price:.2f}")
        
        # 2. Forçar tamanho mínimo para demonstração (0.01 BNB)
        demo_amount = 0.01  # Tamanho mínimo da Binance
        
        # 3. Calcular valor em USDT
        usdt_value = demo_amount * current_price
        print(f"💰 TAMANHO DA ORDEM: {demo_amount} BNB (${usdt_value:.2f} USDT)")
        
        # 4. Executar ordem de COMPRA de mercado (para demo rápida)
        print("🚀 EXECUTANDO ORDEM DE COMPRA...")
        
        order = scalper.exchange.create_market_buy_order(
            symbol='BNB/USDT:USDT',
            amount=demo_amount
        )
        
        print(colored(f"✅ ORDEM EXECUTADA COM SUCESSO!", 'green'))
        print(f"📋 ID da Ordem: {order['id']}")
        print(f"🔢 Quantidade: {order['amount']} BNB")
        print(f"💵 Preço Médio: ${order['average']:.2f}")
        print(f"💸 Custo: ${order['cost']:.2f} USDT")
        
        # 5. Mostrar posição aberta
        print("\n📈 POSIÇÃO ABERTA:")
        print(f"   • Ativo: BNB")
        print(f"   • Quantidade: {demo_amount}")
        print(f"   • Entry: ${order['average']:.2f}")
        print(f"   • Valor: ${usdt_value:.2f} USDT")
        
        # 6. Preparar para fechar a posição (venda demo)
        print("\n⏰ AGUARDANDO 10 SEGUNDOS PARA FECHAR POSIÇÃO...")
        time.sleep(10)
        
        # 7. Fechar posição com venda de mercado
        print("🔒 FECHANDO POSIÇÃO...")
        sell_order = scalper.exchange.create_market_sell_order(
            symbol='BNB/USDT:USDT',
            amount=demo_amount
        )
        
        print(colored(f"✅ POSIÇÃO FECHADA COM SUCESSO!", 'green'))
        print(f"📋 ID da Ordem: {sell_order['id']}")
        print(f"🔢 Quantidade: {sell_order['amount']} BNB")
        print(f"💵 Preço Médio: ${sell_order['average']:.2f}")
        
        # 8. Calcular PnL da demo
        entry_value = order['cost']
        exit_value = sell_order['cost']
        pnl = exit_value - entry_value
        
        print(f"\n📊 RESULTADO DA DEMO:")
        print(f"   • Entry: ${order['average']:.2f}")
        print(f"   • Exit: ${sell_order['average']:.2f}")
        print(f"   • PnL: ${pnl:.4f} USDT")
        
        if pnl > 0:
            print(colored(f"   🎉 LUCRO: ${pnl:.4f}", 'green'))
        else:
            print(colored(f"   🔻 PREJUÍZO: ${abs(pnl):.4f}", 'red'))
        
        print("\n🎬 DEMO FINALIZADA - PRONTO PARA GRAVAÇÃO DO VÍDEO!")
        
    except Exception as e:
        print(colored(f"❌ ERRO NA DEMO: {str(e)}", 'red'))
        
    finally:
        # Fechar conexão
        scalper.exchange.close()

if __name__ == "__main__":
    demo_trade()