import ccxt
import time
import os
from termcolor import colored
from dotenv import load_dotenv

class AsterMonitor:
    def __init__(self):
        # Load Env explicitly
        load_dotenv("config/.env")
        
        # ASTER is tracked via Binance Spot (based on user input)
        self.symbol = "ASTER/USDT" 
        self.target_price = 0.53 # Baseline from user info
        
        # Load Aster Keys
        self.api_key = os.getenv("ASTER_API_KEY")
        self.secret = os.getenv("ASTER_SECRET")
        
        if self.api_key:
            print("[SYSTEM] ASTER DEX KEYS: DETECTED & LOADED")
        else:
            print("[WARNING] ASTER DEX KEYS: NOT FOUND")


        
    def check_aster_health(self, exchange):
        try:
            # Check if ASTER is listed/tradable on the connected exchange
            # Note: User mentioned it's on Binance Spot with Seed Tag
            
            ticker = exchange.fetch_ticker(self.symbol)
            price = ticker['last']
            change_24h = ticker['percentage']
            
            print(f"[ASTER] TOKEN STATUS | PRICE: ${price:.4f} | CHANGE_24H: {change_24h:+.2f}%")
            
            # Simple Arbitrage/Alert Logic
            if price < 0.50:
                print("   >>> [SIGNAL] VALUE ZONE DETECTED (BELOW $0.50)")
            elif price > 0.80:
                print("   >>> [SIGNAL] MOMENTUM SPIKE (ABOVE $0.80)")
                
            return {"price": price, "change": change_24h}
            
        except Exception as e:

            # Silent fail if token not found (might not be listed on Futures yet)
            # print(colored(f"⚠️ Aster Monitor: {str(e)}", "yellow"))
            return None

    def simulate_dark_pool_split(self, total_quantity):
        """
        Simulates Aster's 'Hidden Order' logic by splitting a large order
        into random smaller chunks to avoid market impact.
        """
        import random
        
        chunks = []
        remaining = total_quantity
        
        while remaining > 0:
            if remaining < 10: # Minimum dust
                chunks.append(remaining)
                break
                
            # Split into 10% - 30% chunks
            chunk = remaining * random.uniform(0.1, 0.3)
            chunk = round(chunk, 2)
            chunks.append(chunk)
            remaining -= chunk
            
        return chunks
