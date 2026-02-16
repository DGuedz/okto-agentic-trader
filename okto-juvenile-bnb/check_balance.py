#!/usr/bin/env python3
"""
Verificar saldo na Binance
"""

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'ops'))

from scalp_rsi import ScalpTentacle

def check_balance():
    print("🔍 VERIFICANDO SALDO NA BINANCE...")
    
    scalper = ScalpTentacle()
    
    try:
        balance = scalper.exchange.fetch_balance()
        
        print("💰 SALDOS:")
        print(f"   USDT Livre: {balance['USDT']['free']}")
        print(f"   USDT Total: {balance['USDT']['total']}")
        print(f"   BNB Livre: {balance['BNB']['free']}")
        print(f"   BNB Total: {balance['BNB']['total']}")
        
        # Verificar se há margem suficiente
        usdt_free = float(balance['USDT']['free'])
        if usdt_free < 10:
            print("❌ SALDO INSUFICIENTE - Precisa de pelo menos $10 USDT")
        else:
            print("✅ SALDO SUFICIENTE para demonstração")
            
    except Exception as e:
        print(f"❌ ERRO: {e}")

if __name__ == "__main__":
    check_balance()