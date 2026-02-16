import os
import time
from web3 import Web3
from dotenv import load_dotenv
from termcolor import colored
from src.safety_rails import SafetyRails

# Load environment variables
load_dotenv('config/.env')

class AsterFarmer:
    """
    Aster Tentacle: The Yield Farming Module.
    Connects to Aster DEX on BNB Chain to deposit profits and harvest yield.
    """
    def __init__(self):
        self.rails = SafetyRails()
        self.w3 = self.rails.w3
        self.account = self.w3.eth.account.from_key(os.getenv('OKTO_PK'))
        self.aster_vault_address = "0x0000000000000000000000000000000000000000" # TODO: Replace with actual Aster Vault
        print(colored(f"[ASTER] Tentacle Initialized. Wallet: {self.account.address[:6]}...", "magenta"))

    def check_yield(self):
        """
        Checks pending yield in the Aster Vault.
        """
        if not self.rails.check_gas():
            print(colored("[ASTER] Gas too high. Skipping yield check.", "yellow"))
            return 0.0

        print(colored("[ASTER] Scanning for yield...", "magenta"))
        # Simulation for now
        simulated_yield = 0.0
        # In real impl, we would call: contract.functions.pendingReward(self.account.address).call()
        return simulated_yield

    def deposit_profits(self, amount_bnb):
        """
        Deposits BNB profits into the Aster Vault.
        """
        if not self.rails.check_gas():
            print(colored("[ASTER] Gas too high. Skipping deposit.", "yellow"))
            return False

        print(colored(f"[ASTER] Depositing {amount_bnb} BNB to Vault...", "magenta"))
        # Simulation
        time.sleep(1)
        print(colored(f"[ASTER] ✅ Deposit Confirmed: {amount_bnb} BNB", "green"))
        return True

    def harvest(self):
        """
        Harvests yield and reinvests (Auto-Compound).
        """
        pending = self.check_yield()
        if pending > 0:
            print(colored(f"[ASTER] Harvesting {pending} ASTER...", "magenta"))
            # Simulation
            time.sleep(1)
            print(colored("[ASTER] ✅ Harvest Complete.", "green"))
            return True
        else:
            print(colored("[ASTER] No yield to harvest.", "blue"))
            return False

if __name__ == "__main__":
    farmer = AsterFarmer()
    farmer.check_yield()
