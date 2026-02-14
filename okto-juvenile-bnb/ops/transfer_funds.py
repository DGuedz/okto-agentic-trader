import os
import sys
from termcolor import colored
from dotenv import load_dotenv
from web3 import Web3
import time

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def transfer_to_binance():
    # Load env
    load_dotenv("config/.env")
    
    pk = os.getenv("OKTO_PK")
    rpc = os.getenv("OKTO_RPC")
    # HARDCODED DESTINATION FOR SAFETY (Retrieved via API in previous step)
    binance_address = "0x6227f03146231e8430fca3d232fa3ee919a3167c"
    
    if not pk or not rpc:
        print(colored("❌ Missing OKTO_PK or OKTO_RPC", "red"))
        return

    try:
        # Connect to BSC
        w3 = Web3(Web3.HTTPProvider(rpc))
        if not w3.is_connected():
            print(colored("❌ Failed to connect to RPC", "red"))
            return

        account = w3.eth.account.from_key(pk)
        balance_wei = w3.eth.get_balance(account.address)
        balance_bnb = w3.from_wei(balance_wei, 'ether')
        
        print(colored(f"🔐 OKTO VAULT: {balance_bnb:.4f} BNB", "cyan"))
        print(colored(f"🏦 DESTINATION: {binance_address}", "yellow"))
        
        # Calculate Amount (Leave 0.0015 BNB for gas)
        gas_reserve = w3.to_wei(0.0015, 'ether')
        amount_to_send_wei = balance_wei - gas_reserve
        
        if amount_to_send_wei <= 0:
            print(colored("❌ Insufficient funds for gas + transfer", "red"))
            return

        amount_bnb = w3.from_wei(amount_to_send_wei, 'ether')
        print(colored(f"💸 SENDING: {amount_bnb:.4f} BNB", "green", attrs=['bold']))
        
        # Build Transaction
        tx = {
            'nonce': w3.eth.get_transaction_count(account.address),
            'to': w3.to_checksum_address(binance_address),
            'value': int(amount_to_send_wei),
            'gas': 21000,
            'gasPrice': w3.eth.gas_price,
            'chainId': 56
        }
        
        # Sign Transaction
        signed_tx = w3.eth.account.sign_transaction(tx, pk)
        
        # Send Transaction
        print(colored("🚀 Broadcasting transaction...", "white"))
        # Using rawTransaction (camelCase) or raw_transaction (snake_case) depending on version
        # Debugging showed raw_transaction worked previously
        try:
            raw_tx = signed_tx.rawTransaction
        except AttributeError:
            raw_tx = signed_tx.raw_transaction
            
        tx_hash = w3.eth.send_raw_transaction(raw_tx)









        
        print(colored(f"✅ TX SENT! Hash: {w3.to_hex(tx_hash)}", "green", attrs=['bold']))
        print("Waiting for confirmation...")
        
        # Wait for receipt
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        if receipt.status == 1:
            print(colored("🏆 TRANSFER CONFIRMED! Funds are on the way to Binance.", "green", attrs=['bold']))
        else:
            print(colored("❌ TRANSFER FAILED ON-CHAIN", "red"))

    except Exception as e:
        print(colored(f"❌ Error during transfer: {str(e)}", "red"))

if __name__ == "__main__":
    transfer_to_binance()
