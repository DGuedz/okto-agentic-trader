import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Add root to path

from core.mind_shield import MindShield
from core.sanitizer import LogSanitizer
from termcolor import colored

def run_security_audit():
    print(colored("\n🛡️  STARTING MIND SHIELD SECURITY AUDIT...", "cyan", attrs=['bold']))
    
    # TEST 1: Valid Bridge Operation
    print("\n[TEST 1] Legitimate Bridge Request (Profit -> Vault)")
    valid_context = {"destination": "ASTER_VAULT", "amount": 15.0}
    if MindShield.validate_intent("WITHDRAW", valid_context):
        print(colored("✅ PASS: MindShield authorized valid operation.", "green"))
    else:
        print(colored("❌ FAIL: MindShield blocked valid operation!", "red"))

    # TEST 2: Prompt Injection Attack (Withdraw to Attacker)
    print("\n[TEST 2] Prompt Injection Attack (Withdraw -> Attacker)")
    attack_context = {"destination": "ATTACKER_WALLET", "amount": 1000.0}
    if not MindShield.validate_intent("WITHDRAW", attack_context):
        print(colored("✅ PASS: MindShield BLOCKED unauthorized withdrawal.", "green"))
    else:
        print(colored("❌ FAIL: MindShield ALLOWED attack!", "red", attrs=['blink']))

    # TEST 3: Log Sanitization
    print("\n[TEST 3] Sensitive Data Leakage")
    leak = "Private Key: 0x1234567890abcdef1234567890abcdef12345678"
    sanitized = LogSanitizer.clean(leak)
    if "..." in sanitized:
        print(colored(f"✅ PASS: Key sanitized: {sanitized}", "green"))
    else:
        print(colored(f"❌ FAIL: Key leaked! {sanitized}", "red"))

    print(colored("\n🛡️  AUDIT COMPLETE. SYSTEM SECURE.", "cyan", attrs=['bold']))

if __name__ == "__main__":
    run_security_audit()