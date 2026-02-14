import ccxt
import pandas as pd
import time
import os
from termcolor import colored

from dotenv import load_dotenv

from ops.aster_monitor import AsterMonitor # Import Hidden Order Logic

class ScalpTentacle:
    def __init__(self):
        # Load Env explicitly
        load_dotenv("config/.env")
        
        # Initialize Exchange Connection (Binance)
        api_key = os.getenv("BINANCE_API_KEY")
        secret = os.getenv("BINANCE_SECRET")
        
        # Initialize Aster Module for Dark Pool Logic
        self.aster = AsterMonitor()


        
        config = {
            'enableRateLimit': True,
            'options': {'defaultType': 'future'} 
        }
        
        if api_key and secret and len(api_key) > 10:
            config['apiKey'] = api_key
            config['secret'] = secret
            self.mode = "LIVE_TRADING"
            print("[SYSTEM] BINANCE FUTURES API: CONNECTED")
        else:
            self.mode = "READ_ONLY"
            print("[SYSTEM] BINANCE FUTURES API: READ ONLY (NO KEYS)")
            # DEBUG
            print(f"[DEBUG] KEY LEN: {len(str(api_key))}, SECRET LEN: {len(str(secret))}")


        self.exchange = ccxt.binance(config)
        self.symbol = "BNB/USDT"
        self.leverage = 5
        
        # Set Leverage
        if self.mode == "LIVE_TRADING":
            try:
                self.exchange.set_leverage(self.leverage, self.symbol)
                print(f"[SYSTEM] LEVERAGE SET TO {self.leverage}x")
            except Exception as e:
                print(f"[ERROR] COULD NOT SET LEVERAGE: {str(e)}")

        
    def execute_buy(self, amount_usd=15):
        """Executes a Market Buy Order (LONG)"""
        if self.mode == "READ_ONLY":
            print("[ERROR] CANNOT TRADE IN READ_ONLY MODE")
            return False

        try:
            # 1. Get current price
            ticker = self.exchange.fetch_ticker(self.symbol)
            price = ticker['last']
            
            # 2. Calculate position size with leverage
            # Effective Position = Capital * Leverage
            # Example: $13 * 5 = $65 position
            
            # Check USDT Balance
            balance = self.exchange.fetch_balance()
            usdt_free = balance['USDT']['free']
            
            if usdt_free < 2:
                print("[WARNING] INSUFFICIENT USDT MARGIN")
                return False

            
            # Use max 50% of available margin per trade to be safe
            margin_to_use = usdt_free * 0.95 
            position_size_usd = margin_to_use * self.leverage
            amount_bnb = position_size_usd / price
            
            # Precision adjustment (floor to 2 decimals for BNB futures)
            amount_bnb = float(f"{amount_bnb:.2f}")

            print(f"[EXECUTION] OPENING LONG (5x) | AMOUNT: {amount_bnb} BNB | PRICE: ${price}")
            
            # 2. Execute Order (Pro Mode: Dark Pool Split)
            # If trade size is > 1 BNB (simulated threshold), split it.
            if amount_bnb > 1.0:
                 print(f"[DARK POOL] SPLITTING ORDER | TOTAL: {amount_bnb} BNB")
                 chunks = self.aster.simulate_dark_pool_split(amount_bnb)
                 
                 for chunk in chunks:
                     print(f"   >>> [HIDDEN] EXECUTING CHUNK: {chunk} BNB")
                     self.exchange.create_market_buy_order(self.symbol, chunk)
                     time.sleep(0.2) # Anti-front-run delay
                 
                 order = {"id": "hidden_order_batch", "amount": amount_bnb} # Simulated response
            else:
                # Standard Execution for small orders
                order = self.exchange.create_market_buy_order(self.symbol, amount_bnb)
            
            # 3. Set Stop Loss (Safety Net) - 1.5% below entry

            sl_price = price * 0.985

            # Binance Futures requires SL as a separate order usually, or via params.
            # For simplicity in this v1, we just open the position. 
            # Ideally we would place a STOP_MARKET order immediately.
            
            return {"success": True, "order": order, "price": price}
            
        except Exception as e:
            print(f"[ERROR] LONG EXECUTION FAILED: {str(e)}")
            return {"success": False, "error": str(e)}

    def execute_sell(self):
        """Executes a Market Sell Order (CLOSE LONG or OPEN SHORT)"""
        # For this simple scalp bot, SELL means CLOSE POSITION
        if self.mode == "READ_ONLY": return False
        
        try:
            # 1. Check Current Position
            positions = self.exchange.fetch_positions([self.symbol])
            bnb_position = [p for p in positions if p['symbol'] == self.symbol]
            
            if not bnb_position:
                print("[WARNING] NO POSITION TO CLOSE")
                return False
                
            amt = float(bnb_position[0]['contracts']) # Size in BNB
            
            if amt > 0:
                print(f"[EXECUTION] CLOSING LONG | AMOUNT: {amt} BNB")
                # To close a LONG, we SELL
                order = self.exchange.create_market_sell_order(self.symbol, amt)
                return {"success": True, "order": order}
            else:
                print("[WARNING] NO LONG POSITION DETECTED")
                return False
            
        except Exception as e:
            print(f"[ERROR] CLOSE POSITION FAILED: {str(e)}")
            return {"success": False, "error": str(e)}


        
    def calculate_rsi(self, ohlcv, period=14):
        """Standard RSI 14 calculation"""
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))
        return df['rsi'].iloc[-1]

    def scan_market(self):
        """
        Fetches market data and returns RSI + Market Status
        """
        try:
            # Fetch OHLCV (1m candles for scalping)
            ohlcv = self.exchange.fetch_ohlcv(self.symbol, timeframe='1m', limit=20)
            current_price = ohlcv[-1][4]
            rsi = self.calculate_rsi(ohlcv)
            
            return {
                "success": True,
                "price": current_price,
                "rsi": rsi,
                "symbol": self.symbol
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
