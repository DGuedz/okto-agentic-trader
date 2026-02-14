import ccxt
import pandas as pd
from termcolor import colored
import sys
import time

def analyze_market():
    print(colored("🌊 INITIALIZING MULTI-ASSET SCANNER...", "cyan", attrs=['bold']))
    
    try:
        # Connect to Binance Public
        exchange = ccxt.binance({
            'enableRateLimit': True,
            'options': {'defaultType': 'future'} 
        })
        
        # Assets to Scan (High Volatility & Liquidity)
        symbols = ["BNB/USDT", "ETH/USDT", "SOL/USDT", "BTC/USDT", "CAKE/USDT", "DOGE/USDT"]
        
        print(colored(f"📡 Scanning {len(symbols)} assets for surf opportunities...\n", "white"))
        
        for symbol in symbols:
            try:
                # Fetch OHLCV (1m candles for scalping)
                ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1m', limit=50)
                
                if not ohlcv:
                    continue

                df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                current_price = df['close'].iloc[-1]
                
                # Calculate RSI
                period = 14
                delta = df['close'].diff()
                gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
                loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
                rs = gain / loss
                df['rsi'] = 100 - (100 / (1 + rs))
                
                rsi = df['rsi'].iloc[-1]
                
                # Trend Analysis (SMA 20)
                sma_20 = df['close'].rolling(window=20).mean().iloc[-1]
                trend = "BULLISH" if current_price > sma_20 else "BEARISH"
                
                # Volatility (ATR-like: High - Low of last candle)
                last_candle = df.iloc[-1]
                volatility = ((last_candle['high'] - last_candle['low']) / last_candle['low']) * 100
                
                # Formatting Output
                symbol_fmt = f"{symbol:<10}"
                price_fmt = f"${current_price:<10.2f}"
                rsi_color = "green" if rsi < 30 else "red" if rsi > 70 else "white"
                trend_color = "green" if trend == "BULLISH" else "red"
                
                print(f"{symbol_fmt} | {price_fmt} | RSI: " + colored(f"{rsi:.1f}", rsi_color) + f" | Trend: " + colored(trend, trend_color) + f" | Vol: {volatility:.2f}%")
                
                # Signal Logic
                if rsi < 30 and trend == "BULLISH":
                    print(colored(f"   >>> 🏄 SURF SIGNAL: OVERSOLD IN UPTREND (Pullback Buy)", "green", attrs=['bold', 'blink']))
                elif rsi > 70 and trend == "BEARISH":
                    print(colored(f"   >>> 📉 SURF SIGNAL: OVERBOUGHT IN DOWNTREND (Short)", "red", attrs=['bold']))
                elif volatility > 0.5:
                    print(colored(f"   >>> 🌊 HIGH VOLATILITY: Good for Scalping", "cyan"))
                    
                time.sleep(0.2) # Rate limit nice
                
            except Exception as e:
                print(colored(f"⚠️ Error scanning {symbol}: {str(e)}", "yellow"))
                
        print("\n" + colored("✅ SCAN COMPLETE", "green", attrs=['bold']))
        
    except Exception as e:
        print(colored(f"❌ GLOBAL SCAN ERROR: {str(e)}", "red"))

if __name__ == "__main__":
    analyze_market()
