import os
import sys
from termcolor import colored
from dotenv import load_dotenv
from web3 import Web3

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def check_vault_balance():
    # Load env
    load_dotenv("config/.env")
    
    pk = os.getenv("OKTO_PK")
    rpc = os.getenv("OKTO_RPC")
    
    if not pk or not rpc:
        print(colored("❌ Missing OKTO_PK or OKTO_RPC", "red"))
        return

    try:
        w3 = Web3(Web3.HTTPProvider(rpc))
        if not w3.is_connected():
            print(colored("❌ Failed to connect to RPC", "red"))
            return

        account = w3.eth.account.from_key(pk)
        balance_wei = w3.eth.get_balance(account.address)
        balance_bnb = w3.from_wei(balance_wei, 'ether')
        
        print(colored(f"🔐 OKTO VAULT (On-Chain):", "cyan", attrs=['bold']))
        print(colored(f"Address: {account.address}", "white"))
        print(colored(f"Balance: {balance_bnb:.4f} BNB", "green"))
        
    except Exception as e:
        print(colored(f"❌ Error checking vault: {str(e)}", "red"))

if __name__ == "__main__":
    check_vault_balance()
