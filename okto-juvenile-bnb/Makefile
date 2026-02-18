# OKTO ORCHESTRATION
# "Terminal-First" Execution Layer

.PHONY: paper live monitor grid

# Modo Simulado (Paper Trading)
paper:
	@echo "🔍 DIAGNOSTIC..."
	@python3 ops/market_diagnostic.py > state.json
	@cat state.json
	@echo "\n🧠 DECISION..."
	@python3 ops/decide.py state.json > plan.json
	@cat plan.json
	@echo "\n🛰️  MONITOR..."
	@python3 ops/monitor.py plan.json

# Modo Real (Live Execution - CUIDADO)
live:
	@echo "⚠️  LIVE MODE ACTIVE"
	@python3 ops/market_diagnostic.py > state.json
	@python3 ops/decide.py state.json > plan.json
	@python3 ops/execute_live.py plan.json # (Placeholder)
	@python3 ops/monitor.py plan.json

# Loop de Grid (Maker Strategy)
grid:
	@echo "🕸️  STARTING GRID LOOP..."
	@python3 ops/grid_loop.py --symbol BNB/USDT --lower 617.55 --upper 619.45 --grids 4

# Loop de Monitoramento (Watchdog)
watch:
	@while true; do make paper; sleep 60; done
