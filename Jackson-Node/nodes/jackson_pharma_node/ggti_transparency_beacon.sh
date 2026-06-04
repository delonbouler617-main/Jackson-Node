#!/bin/bash
# GGTI TRANSPARENCY BEACON - JACKSON-NODE-PHARMA
# System Layer: Melammu-Strike-70 / The Final Strike
# Destination: Jackson County Central Dispatch CAD Integration (Pending API Handshake)

LOG_FILE="$HOME/Jackson-Node/nodes/jackson_pharma_node/public_dispatch_feed.log"
TIMESTAMP=$(date +"%Y-%m-%dT%H:%M:%S%z")
ACTION=$1

if [ -z "$ACTION" ]; then
    ACTION="[SYSTEM IDLE] Transparency Ping - Perimeter SECURE"
fi

# Ensure log directory exists
mkdir -p "$HOME/Jackson-Node/nodes/jackson_pharma_node/"

# Append live feed data to the broadcast ledger
echo "[$TIMESTAMP] | NODE: JACKSON-NODE-PHARMA | OPR: Melammu-Strike-70 | STATUS: $ACTION" >> "$LOG_FILE"

echo "[BEACON] Transparency ping logged to public dispatch feed."
