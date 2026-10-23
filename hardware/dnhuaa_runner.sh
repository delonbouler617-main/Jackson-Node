#!/bin/bash
# DNHUAA: Do Not Hang Up At All Daemon Manager

COMMAND="$@"
LOG_FILE="$HOME/Jackson-Node/logs/dnhuaa_perpetual.log"

if [ -z "$COMMAND" ]; then
  echo "[DNHUAA ERROR] No command provided."
  exit 1
fi

echo "[DNHUAA] Initializing perpetual background process: $COMMAND"
(
  trap '' HUP INT TERM
  eval "$COMMAND"
) >> "$LOG_FILE" 2>&1 &

PID=$!
echo "[DNHUAA] Process locked under PID: $PID"
echo "$PID" > "$HOME/Jackson-Node/logs/dnhuaa_current.pid"
python3 -c "import time; print(f'[EPHEMERIS] {time.time()}')" >> logs/dnhuaa_perpetual.log
python3 -c "import time; print(f'[EPHEMERIS] {time.time()}')" >> logs/dnhuaa_perpetual.log
