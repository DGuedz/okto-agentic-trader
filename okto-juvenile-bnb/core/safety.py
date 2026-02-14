import time
from web3 import Web3
from termcolor import colored
import os
from dotenv import load_dotenv

def check_network_health(silent=False):
    """
    Verifies if the network is safe for operation.
    Returns: (is_safe, details_dict)
    """
    # Load env to get custom RPC if available
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_env = os.path.join(base_path, 'config', '.env')
    if os.path.exists(config_env): load_dotenv(config_env)
    
    # Use RPC from env or fallback to public
    RPC_URL = os.getenv("OKTO_RPC", "https://bsc-dataseed.binance.org/")
    
    details = {
        "connected": False,
        "gas_price": 0.0,
        "latency_ms": 0,
        "provider": "Unknown",
        "msg": ""
    }
    
    try:
        start_time = time.time()
        w3 = Web3(Web3.HTTPProvider(RPC_URL))
        
        if not w3.is_connected():
            details["msg"] = "Connection Failed"
            if not silent: print(colored("❌ CRITICAL: Cannot connect to BSC RPC", "red"))
            return False, details
            
        latency = (time.time() - start_time) * 1000
        details["latency_ms"] = latency
        details["connected"] = True
        
        # Identify Provider type
        if "alchemy" in RPC_URL:
            details["provider"] = "Alchemy (Private)"
        elif "binance" in RPC_URL:
            details["provider"] = "Public Node"
        else:
            details["provider"] = "Custom RPC"
        
        gas_price_wei = w3.eth.gas_price
        gas_price_gwei = w3.from_wei(gas_price_wei, 'gwei')
        details["gas_price"] = float(gas_price_gwei)
        
        if not silent: 
            print(f"⛽ Current Gas Price: {gas_price_gwei:.2f} Gwei")
            print(f"⏱️  Latency: {latency:.2f}ms")
        
        if gas_price_gwei < 5.0:
            details["msg"] = "Optimal"
            if not silent: print(colored("✅ NETWORK HEALTHY: Gas is cheap", "green"))
            return True, details
        else:
            details["msg"] = "Congested"
            if not silent: print(colored(f"⚠️ NETWORK CONGESTED: Gas {gas_price_gwei:.2f} > 5.0 Gwei", "yellow"))
            return False, details
            
    except Exception as e:
        details["msg"] = str(e)
        if not silent: print(colored(f"❌ SAFETY CHECK FAILED: {str(e)}", "red"))
        return False, details

if __name__ == "__main__":
    check_network_health()
