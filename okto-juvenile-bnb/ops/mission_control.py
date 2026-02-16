from termcolor import colored

class MissionControl:
    def __init__(self):
        self.phases = [
            {"name": "SEED", "target": 10.00, "next": "ALPHA"},
            {"name": "ALPHA", "target": 15.00, "next": "BETA"},
            {"name": "BETA", "target": 20.00, "next": "GAMMA"},
            {"name": "GAMMA", "target": 50.00, "next": "OMEGA"},
            {"name": "OMEGA", "target": 100.00, "next": "MOON"}
        ]
        self.game_over_threshold = 9.50 # $10 - 5%
        
        # ASTER FARMING TRACKING
        self.total_yield_farmed = 0.0 # Total ASTER tokens farmed
        self.unallocated_profit = 0.0 # Profit ready to be bridged to Vault

    def update_yield(self, amount):
        self.total_yield_farmed += amount
        
    def add_profit(self, amount):
        self.unallocated_profit += amount
        
    def reset_profit(self):
        self.unallocated_profit = 0.0

    def analyze_status(self, current_balance_usd):
        """
        Determines current phase and health status.
        """
        status = {
            "phase": "UNKNOWN",
            "progress": 0.0,
            "health": "HEALTHY",
            "message": ""
        }

        # 1. Check Game Over (Dust Risk)
        if current_balance_usd < self.game_over_threshold:
            status["health"] = "CRITICAL"
            status["message"] = f"💀 GAME OVER RISK! Balance (${current_balance_usd:.2f}) < Threshold (${self.game_over_threshold:.2f})"
            return status

        # 2. Determine Phase
        current_phase = self.phases[0]
        for phase in self.phases:
            if current_balance_usd >= phase["target"]:
                current_phase = phase
            else:
                break # We are in the previous phase working towards this one
        
        # Find next target
        next_phase_name = current_phase["next"]
        next_target = 0.0
        for p in self.phases:
            if p["name"] == next_phase_name:
                next_target = p["target"]
                break
        
        if next_target == 0.0: # Reached Omega
            status["phase"] = "OMEGA COMPLETED"
            status["progress"] = 100.0
            status["message"] = "🏆 MISSION ACCOMPLISHED"
        else:
            status["phase"] = current_phase["name"]
            # Calculate progress to next level
            # (Current - Current_Base) / (Next - Current_Base)
            base = current_phase["target"]
            needed = next_target - base
            gained = current_balance_usd - base
            pct = (gained / needed) * 100 if needed > 0 else 0
            
            status["progress"] = pct
            status["message"] = f"🚀 PHASE: {current_phase['name']} >> {next_phase_name} ({pct:.1f}%)"

        return status

    def print_hud(self, current_balance_usd):
        status = self.analyze_status(current_balance_usd)
        
        print("\n" + "="*40)
        print(colored(" 🚩 MISSION CONTROL: BOOTSTRAP ($10->$100)", "white", attrs=['bold']))
        print("="*40)
        
        if status["health"] == "CRITICAL":
            print(colored(status["message"], "red", attrs=['blink']))
        else:
            color = "cyan"
            if status["phase"] == "OMEGA": color = "magenta"
            if status["phase"] == "SEED": color = "yellow"
            
            print(f"💰 BALANCE: ${current_balance_usd:.2f}")
            print(colored(status["message"], color))
            
            # Visual Bar
            bar_len = 20
            filled = int((status["progress"] / 100) * bar_len)
            bar = "█" * filled + "░" * (bar_len - filled)
            print(f"[{bar}] {status['progress']:.1f}% to Next Level")
            
        print("="*40 + "\n")
