import ccxt
import pandas as pd
import numpy as np
import json
import time
import sys

def fetch_market_data(symbol='BNB/USDT'):
    try:
        exchange = ccxt.binance({'enableRateLimit': True})
        
        # 1. Order Book (OBI)
        orderbook = exchange.fetch_order_book(symbol, limit=20)
        bids = sum([x[1] for x in orderbook['bids']])
        asks = sum([x[1] for x in orderbook['asks']])
        obi = (bids - asks) / (bids + asks) if (bids + asks) > 0 else 0
        spread = (orderbook['asks'][0][0] - orderbook['bids'][0][0]) / orderbook['asks'][0][0] * 100
        
        # 2. OHLCV (RSI + ATR)
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe='5m', limit=50)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        
        # RSI 14
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))
        current_rsi = df['rsi'].iloc[-1]
        
        # ATR 14 (Volatilidade)
        df['tr'] = np.maximum(df['high'] - df['low'], 
                              np.maximum(abs(df['high'] - df['close'].shift()), 
                                         abs(df['low'] - df['close'].shift())))
        df['atr'] = df['tr'].rolling(window=14).mean()
        current_atr = df['atr'].iloc[-1]
        atr_pct = (current_atr / df['close'].iloc[-1]) * 100
        
        market_state = {
            "symbol": symbol,
            "price": df['close'].iloc[-1],
            "obi": round(obi, 4),
            "rsi": round(current_rsi, 2),
            "atr": round(current_atr, 4),
            "atr_pct": round(atr_pct, 4),
            "spread_pct": round(spread, 4),
            "timestamp": int(time.time())
        }
        
        # If running as script, print JSON for piping. If imported, return dict.
        if __name__ == "__main__":
            print(json.dumps(market_state))
        return market_state
            
    except Exception as e:
        if __name__ == "__main__":
            print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    fetch_market_data()
