#!/bin/bash
LOG_FILE="logs/grid.live.log"
PID_FILE="logs/grid.pid"

mkdir -p logs

echo "🛡️  WATCHDOG ACTIVE: Monitoring Grid Loop..."
echo "------------------------------------------------"

# Mata instância anterior se existir
if [ -f "$PID_FILE" ]; then
    kill -9 $(cat "$PID_FILE") 2>/dev/null
    rm "$PID_FILE"
fi

# Inicia Grid com parâmetros otimizados
nohup python3 ops/grid_loop.py \
    --symbol BNB/USDT \
    --lower 617.55 --upper 619.45 \
    --grids 5 \
    > "$LOG_FILE" 2>&1 &

echo $! > "$PID_FILE"
echo "✅ Grid Started (PID: $(cat $PID_FILE))"
echo "📊 Monitoring Log (Tail -f):"
echo "------------------------------------------------"

tail -f "$LOG_FILE"
