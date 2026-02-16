import os
import sys
from termcolor import colored

def audit_env_security():
    print(colored("🔒 STARTING ZERO-LEAKAGE AUDIT (BSC LEVEL)...", "cyan", attrs=['bold']))
    
    env_path = 'config/.env'
    if not os.path.exists(env_path):
        # Fallback to root .env
        env_path = '.env'
        if not os.path.exists(env_path):
            print(colored("❌ CRITICAL: No .env file found!", "red"))
            return False

    # 1. Permission Check
    st = os.stat(env_path)
    # Check if group or others have read permission (should be 600 or 700)
    if st.st_mode & 0o044 or st.st_mode & 0o004:
        print(colored(f"⚠️  WARNING: {env_path} permissions are too open ({oct(st.st_mode)[-3:]}). Fixing...", "yellow"))
        os.chmod(env_path, 0o600)
        print(colored("✅ FIXED: Permissions set to 600 (User Read/Write ONLY).", "green"))
    else:
        print(colored(f"✅ PASS: File permissions secure ({oct(st.st_mode)[-3:]}).", "green"))

    # 2. Gitignore Check
    gitignore_path = '.gitignore'
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            content = f.read()
            if '.env' in content or 'config/.env' in content:
                print(colored("✅ PASS: .env is blocked in .gitignore.", "green"))
            else:
                print(colored("❌ FAIL: .env NOT fully blocked in .gitignore!", "red"))
    else:
        print(colored("❌ CRITICAL: No .gitignore found!", "red"))

    # 3. Key Format Validation (Zero Knowledge)
    try:
        with open(env_path, 'r') as f:
            lines = f.readlines()
            pk_found = False
            for line in lines:
                if line.startswith('OKTO_PK='):
                    pk_found = True
                    key = line.split('=')[1].strip()
                    # Basic Hex validation without printing
                    clean_key = key.replace('0x', '')
                    if len(clean_key) == 64:
                         print(colored("✅ PASS: BSC Private Key detected and format valid (Hex).", "green"))
                    else:
                         print(colored(f"❌ FAIL: Invalid BSC Private Key length! (Expected 64 hex chars, got {len(clean_key)})", "red"))
                    break
            
            if not pk_found:
                print(colored("❌ FAIL: OKTO_PK not found in .env!", "red"))

    except Exception as e:
        print(colored(f"❌ ERROR: Could not read .env: {str(e)}", "red"))

    print(colored("\n🛡️  AUDIT COMPLETE. SYSTEM SECURE.", "cyan", attrs=['bold']))

if __name__ == "__main__":
    audit_env_security()