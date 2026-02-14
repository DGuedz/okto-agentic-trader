import ccxt
import time
import os
import sys
from termcolor import colored

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def analyze_obi(symbol="BNB/USDT", depth=20):
    """
    Analyzes Order Book Imbalance (OBI)
    OBI = (Bid Vol - Ask Vol) / (Bid Vol + Ask Vol)
    Range: -1 (Strong Sell Pressure) to +1 (Strong Buy Pressure)
    """
    try:
        exchange = ccxt.binance({'enableRateLimit': True})
        
        print(colored(f"📖 READING ORDER BOOK: {symbol} (Depth {depth})", "cyan", attrs=['bold']))
        
        # Fetch Order Book
        orderbook = exchange.fetch_order_book(symbol, limit=depth)
        
        bids = orderbook['bids']
        asks = orderbook['asks']
        
        # Calculate Volumes
        bid_vol = sum([bid[1] for bid in bids]) # Price, Volume
        ask_vol = sum([ask[1] for ask in asks])
        
        # Calculate Imbalance
        total_vol = bid_vol + ask_vol
        obi = (bid_vol - ask_vol) / total_vol
        
        # Visualization
        print("-" * 50)
        print(f"🟢 BID VOLUME: {bid_vol:.4f} BNB")
        print(f"🔴 ASK VOLUME: {ask_vol:.4f} BNB")
        print("-" * 50)
        
        # OBI Interpretation
        if obi > 0.2:
            status = "STRONG BUYING PRESSURE 🐂"
            color = "green"
        elif obi > 0.05:
            status = "MILD BUYING PRESSURE 📈"
            color = "light_green"
        elif obi < -0.2:
            status = "STRONG SELLING PRESSURE 🐻"
            color = "red"
        elif obi < -0.05:
            status = "MILD SELLING PRESSURE 📉"
            color = "light_red"
        else:
            status = "NEUTRAL / BALANCED ⚖️"
            color = "yellow"
            
        print(colored(f"📊 OBI INDEX: {obi:.4f}", color, attrs=['bold']))
        print(colored(f"🗣️ THE BOOK SAYS: {status}", color, attrs=['bold']))
        print("-" * 50)
        
        # Price Wall Detection
        max_bid = max(bids, key=lambda x: x[1])
        max_ask = max(asks, key=lambda x: x[1])
        
        print(f"🧱 BUY WALL:  {max_bid[1]:.2f} BNB @ ${max_bid[0]:.2f}")
        print(f"🧱 SELL WALL: {max_ask[1]:.2f} BNB @ ${max_ask[0]:.2f}")
        
        return {
            "obi": obi,
            "status": status,
            "sell_wall_price": max_ask[0],
            "buy_wall_price": max_bid[0]
        }
        
    except Exception as e:
        print(colored(f"❌ Error reading book: {str(e)}", "red"))
        return None

if __name__ == "__main__":
    analyze_obi()
