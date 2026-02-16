import yaml
import os
from web3 import Web3
from dotenv import load_dotenv

# Carregar variáveis de ambiente (tentando config/.env primeiro)
load_dotenv('config/.env')

class SafetyRails:
    def __init__(self, spec_path='specs/genesis.yaml'):
        with open(spec_path, 'r') as f:
            self.spec = yaml.safe_load(f)
        
        # Prioriza RPC do env, fallback para public node da BSC
        rpc_url = os.getenv('BSC_RPC_URL') or os.getenv('RPC_URL') or 'https://bsc-dataseed.binance.org/'
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))

    def check_gas(self):
        """Valida se o Gás da rede está dentro do limite da Spec"""
        try:
            curr_gas = self.w3.eth.gas_price
            # Busca max_gas em safety_thresholds
            max_gas_gwei = self.spec.get('safety_thresholds', {}).get('max_gas', 10)
            max_gas_wei = max_gas_gwei * 10**9 # Gwei to Wei
            
            print(f"[SAFETY] Gas Check: Current={curr_gas/10**9:.2f} Gwei | Max={max_gas_gwei} Gwei")
            return curr_gas <= max_gas_wei
        except Exception as e:
            print(f"[ERROR][SAFETY] Gas check failed: {e}")
            return False

    def simulate_tx(self, tx_params):
        """Simula transação (Dry-run) antes da execução real"""
        try:
            self.w3.eth.call(tx_params)
            return True
        except Exception as e:
            print(f"[ERROR][SAFETY]: Simulação falhou: {e}")
            return False

# Execução de teste se rodado diretamente
if __name__ == "__main__":
    print("🛡️  INITIATING VSC SAFETY RAILS...")
    rails = SafetyRails()
    if rails.w3.is_connected():
        print(f"✅ CONNECTED TO CHAIN ID: {rails.w3.eth.chain_id}")
        if rails.check_gas():
            print("✅ GAS STATUS: GREEN")
        else:
            print("❌ GAS STATUS: RED (TOO HIGH)")
    else:
        print("❌ FAILED TO CONNECT TO RPC")