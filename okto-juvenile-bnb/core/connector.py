import os
import re
from dotenv import load_dotenv
from web3 import Web3
from termcolor import colored

def connect_vault():
    """
    Securely connects to the Vault (Wallet) using credentials from .env
    Returns: {status: bool, address: str, balance_bnb: float, w3: object, msg: str}
    """
    # 1. Load Environment Variables (Multiple Paths)
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    potential_paths = [
        os.path.join(base_path, 'config', '.env'),
        os.path.join(base_path, 'venv', 'okto-juvenile-bnb', '.env'),
        os.path.join(base_path, '.env')
    ]
    
    checked_paths = []
    
    # Try loading from paths until found
    for p in potential_paths:
        if os.path.exists(p):
            checked_paths.append(p)
            load_dotenv(p)
            # Check if this file has the goods
            pk_test = os.getenv("OKTO_PK")
            if pk_test and not pk_test.startswith("000000"):
                break # Found a good one
    
    result = {
        "status": False,
        "address": "UNKNOWN",
        "balance_bnb": 0.0,
        "w3": None,
        "msg": ""
    }
    
    try:
        # 2. Retrieve Secrets (Smart Recovery)
        pk = os.getenv("OKTO_PK")
        
        # Scavenge for key if missing or placeholder
        if not pk or pk.startswith("000000") or len(pk) < 64:
            # Try to read all files directly to find the key
            for p in potential_paths:
                if not os.path.exists(p): continue
                try:
                    with open(p, 'r') as f:
                        content = f.read()
                        matches = re.findall(r'[a-fA-F0-9]{64}', content)
                        for match in matches:
                            if not match.startswith("000000"):
                                pk = match
                                break
                    if pk and not pk.startswith("000000"):
                        break
                except Exception:
                    pass

        if not pk or pk.startswith("000000"):
            paths_str = "\n".join(checked_paths)
            result["msg"] = f"No valid OKTO_PK found in:\n{paths_str}"
            return result
            
        rpc = os.getenv("OKTO_RPC", "https://bsc-dataseed.binance.org/")
            
        # 3. Initialize Web3
        w3 = Web3(Web3.HTTPProvider(rpc))
        if not w3.is_connected():
            result["msg"] = "RPC Connection Failed"
            return result
            
        # 4. Derive Address & Check Balance
        if not pk.startswith("0x"):
            pk = "0x" + pk
            
        account = w3.eth.account.from_key(pk)
        address = account.address
        balance_wei = w3.eth.get_balance(address)
        balance_bnb = float(w3.from_wei(balance_wei, 'ether'))
        
        result["status"] = True
        result["address"] = address
        result["balance_bnb"] = balance_bnb
        result["w3"] = w3
        result["msg"] = "Vault Connected"
        
        return result
        
    except Exception as e:
        result["msg"] = f"Vault Error: {str(e)}"
        return result

if __name__ == "__main__":
    res = connect_vault()
    if res['status']:
        print(colored(f"✅ Vault Connected: {res['address']} | Balance: {res['balance_bnb']} BNB", "green"))
    else:
        print(colored(f"❌ Vault Error: {res['msg']}", "red"))
