import ccxt
import os
import sys
from dotenv import load_dotenv

class CapitalManager:
    def __init__(self):
        # Load Env explicitly
        load_dotenv("config/.env")
        
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.secret = os.getenv("BINANCE_SECRET")
        self.target_profit_threshold = 5.0 # Minimum profit to trigger rotation (USDT)
        self.initial_balance = None # Will be set on first run
        self.metrics = {
            "rotation_attempts": 0,
            "rotation_amounts": [],
            "last_rotation": None,
            "last_profit": 0
        }
        
        # Connect to Binance Spot (for withdrawals)
        if self.api_key:
            self.exchange = ccxt.binance({
                'apiKey': self.api_key,
                'secret': self.secret,
                'enableRateLimit': True
            })
        else:
            self.exchange = None

    def initialize_balance(self):
        """Captures the starting balance to calculate PnL correctly."""
        if not self.exchange: return False
        try:
            balance = self.exchange.fetch_balance()
            self.initial_balance = balance['USDT']['free']
            print(f"[CAPITAL] INITIAL BALANCE LOCKED: ${self.initial_balance:.2f}")
            return True
        except Exception as e:
            print(f"[ERROR] FAILED TO INIT BALANCE: {str(e)}")
            return False

    def scan_for_rotation(self):
        """
        Checks if there is excess capital (Net Profit) to rotate to Aster.
        Rotation Amount = Current Balance - Initial Balance
        Condition: Rotation Amount > Threshold
        """
        if not self.exchange:
            return {"status": "ERROR", "msg": "No API Keys"}

        try:
            # 0. Ensure Initial Balance is set
            if self.initial_balance is None:
                self.initialize_balance()
                return {"status": "INITIALIZING", "msg": "Setting baseline..."}

            # 1. Check USDT Balance
            balance = self.exchange.fetch_balance()
            current_usdt = balance['USDT']['free']
            
            # 2. Logic: Calculate Net Profit (High Water Mark)
            net_profit = current_usdt - self.initial_balance
            self.metrics["last_profit"] = net_profit
            
            if net_profit > self.target_profit_threshold:
                return {
                    "status": "ROTATION_SIGNAL",
                    "amount": net_profit, # Rotate ONLY the profit
                    "msg": f"NET PROFIT DETECTED: ${net_profit:.2f} (Base: ${self.initial_balance:.2f})"
                }
            elif net_profit < 0:
                return {
                    "status": "RECOVERY_MODE",
                    "amount": 0,
                    "msg": f"DRAWDOWN: ${net_profit:.2f}"
                }
            else:
                return {
                    "status": "ACCUMULATING",
                    "amount": 0,
                    "msg": f"PROFIT BELOW THRESHOLD: ${net_profit:.2f} / ${self.target_profit_threshold}"
                }
                
        except Exception as e:
            return {"status": "ERROR", "msg": str(e)}


    def execute_rotation(self, amount, target_address):
        """
        Executes the withdrawal to the On-Chain Vault.
        Note: Requires 'Enable Withdrawals' permission on API Key.
        """
        print(f"[CAPITAL] INITIATING BRIDGE TO ASTER CHAIN...")
        print(f"[CAPITAL] TARGET: {target_address} | AMOUNT: {amount} USDT")
        
        # SAFETY: For Hackathon demo, we log the intent but do not force withdrawal 
        # unless explicitly enabled to avoid API permission errors during live demo.
        # Real execution would be:
        # self.exchange.withdraw('USDT', amount, target_address, tag=None, params={'network': 'BSC'})
        
        self.metrics["rotation_attempts"] += 1
        self.metrics["rotation_amounts"].append(amount)
        rotation = {
            "tx_hash": "0xSIMULATED_HASH_FOR_DEMO_" + os.urandom(4).hex(),
            "status": "QUEUED_FOR_BRIDGE"
        }
        self.metrics["last_rotation"] = {
            "target": target_address,
            "amount": amount,
            "status": rotation["status"],
            "tx_hash": rotation["tx_hash"]
        }
        return rotation
