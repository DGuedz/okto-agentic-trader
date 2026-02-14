import ccxt
import os
import sys
from termcolor import colored
from dotenv import load_dotenv

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def check_total_balance():
    load_dotenv("config/.env")
    
    api_key = os.getenv("BINANCE_API_KEY")
    secret = os.getenv("BINANCE_SECRET")
    
    if not api_key:
        print(colored("❌ ERRO: Chaves de API não encontradas no .env", "red"))
        return

    try:
        print(colored("\n🔎 RASTREADOR DE CAPITAL OKTO", "cyan", attrs=['bold']))
        print("-" * 40)
        
        # 1. Conexão SPOT (Carteira à vista)
        spot_exchange = ccxt.binance({'apiKey': api_key, 'secret': secret})
        spot_balance = spot_exchange.fetch_balance()
        
        spot_total_usd = 0
        print(colored("🏠 CARTEIRA SPOT (Depósitos/Hold):", "yellow"))
        for currency, amount in spot_balance['total'].items():
            if amount > 0:
                # Tenta pegar preço em USD para estimativa
                usd_val = 0
                if currency == 'USDT':
                    usd_val = amount
                else:
                    try:
                        ticker = spot_exchange.fetch_ticker(f"{currency}/USDT")
                        usd_val = amount * ticker['last']
                    except:
                        pass # Ignora se não achar par
                
                if usd_val > 0.1: # Filtra poeira
                    print(f"   - {currency}: {amount:.6f} (~${usd_val:.2f})")
                    spot_total_usd += usd_val
        
        if spot_total_usd == 0:
            print("   (Vazia - Capital migrado ou não depositado)")

        # 2. Conexão FUTURES (Onde o bot opera)
        futures_exchange = ccxt.binance({
            'apiKey': api_key, 
            'secret': secret,
            'options': {'defaultType': 'future'}
        })
        futures_balance = futures_exchange.fetch_balance()
        
        futures_total_usd = futures_balance['USDT']['total']
        futures_free_usd = futures_balance['USDT']['free']
        futures_used_usd = futures_balance['USDT']['used']
        
        print(colored("\n⚔️  CARTEIRA FUTUROS (Operacional):", "green"))
        print(f"   - Saldo Total:   ${futures_total_usd:.2f}")
        print(f"   - Margem Livre:  ${futures_free_usd:.2f}")
        print(f"   - Em Operação:   ${futures_used_usd:.2f}")
        
        # 3. Posições Abertas
        positions = futures_exchange.fetch_positions()
        active_positions = [p for p in positions if float(p['entryPrice']) > 0 and float(p['contracts']) > 0]
        
        if active_positions:
            print(colored("\n📉 POSIÇÕES ABERTAS:", "red"))
            for p in active_positions:
                pnl = float(p['unrealizedPnl'])
                pnl_color = "green" if pnl >= 0 else "red"
                print(f"   - {p['symbol']} ({p['side']}): {p['contracts']} contratos")
                print(f"     Entrada: ${p['entryPrice']} | PnL: " + colored(f"${pnl:.2f}", pnl_color))
        else:
            print(colored("\n😴 Nenhuma posição aberta no momento.", "white"))

        print("-" * 40)
        total_equity = spot_total_usd + futures_total_usd
        print(colored(f"💎 PATRIMÔNIO TOTAL IDENTIFICADO: ${total_equity:.2f}", "cyan", attrs=['bold']))
        print("-" * 40)

    except Exception as e:
        print(colored(f"❌ ERRO DE CONEXÃO: {str(e)}", "red"))

if __name__ == "__main__":
    check_total_balance()
