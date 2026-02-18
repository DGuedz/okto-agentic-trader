import json
import sys
import os

def decide_trade(state_file):
    try:
        with open(state_file, 'r') as f:
            state = json.load(f)
            
        atr_pct = state['atr_pct']
        obi = state['obi']
        rsi = state['rsi']
        atr = state['atr']
        price = state['price']
        
        decision = {
            "action": "NO_TRADE",
            "reason": "Wait for setup",
            "params": {}
        }
        
        # 1. Regime Gate (Volatilidade)
        if atr_pct < 0.08:
            decision['reason'] = f"Dead Market (ATR {atr_pct}%)"
            print(json.dumps(decision))
            return
        if atr_pct > 0.60:
            decision['reason'] = f"Too Volatile (ATR {atr_pct}%)"
            print(json.dumps(decision))
            return
            
        # 2. Direction Gate (OBI) - BIDIRECIONAL
        if obi > 0.20:
            # LONG SETUP
            if rsi < 70:
                decision['action'] = "ALLOW_LONG"
                decision['reason'] = "OBI Bullish + RSI Safe"
            elif rsi < 78:
                if obi > 0.4:
                    decision['action'] = "ALLOW_LONG"
                    decision['reason'] = "OBI Strong Bullish > RSI High"
                else:
                    decision['reason'] = f"RSI Overbought ({rsi})"
            else:
                decision['reason'] = f"RSI Extreme ({rsi})"
                
        elif obi < -0.20:
            # SHORT SETUP
            if rsi > 30:
                decision['action'] = "ALLOW_SHORT"
                decision['reason'] = "OBI Bearish + RSI Safe"
            elif rsi > 22:
                if obi < -0.4:
                    decision['action'] = "ALLOW_SHORT"
                    decision['reason'] = "OBI Strong Bearish > RSI Low"
                else:
                    decision['reason'] = f"RSI Oversold ({rsi})"
            else:
                decision['reason'] = f"RSI Extreme Low ({rsi})"
        else:
            decision['reason'] = f"OBI Neutral ({obi})"
            
        # 3. Sizing & Risk Params
        if decision['action'] == "ALLOW_LONG":
            sl_price = price - (1.2 * atr)
            tp1_price = price + (0.8 * atr)
            tp2_price = price + (1.6 * atr)
            
            decision['params'] = {
                "symbol": state['symbol'],
                "leverage": 20,
                "side": "BUY",
                "entry": price,
                "sl": round(sl_price, 2),
                "tp1": round(tp1_price, 2),
                "tp2": round(tp2_price, 2),
                "atr": atr
            }
            
        elif decision['action'] == "ALLOW_SHORT":
            sl_price = price + (1.2 * atr)
            tp1_price = price - (0.8 * atr)
            tp2_price = price - (1.6 * atr)
            
            decision['params'] = {
                "symbol": state['symbol'],
                "leverage": 20,
                "side": "SELL",
                "entry": price,
                "sl": round(sl_price, 2),
                "tp1": round(tp1_price, 2),
                "tp2": round(tp2_price, 2),
                "atr": atr
            }
            
        print(json.dumps(decision))
        
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        decide_trade(sys.argv[1])
    else:
        print(json.dumps({"error": "No state file provided"}))
