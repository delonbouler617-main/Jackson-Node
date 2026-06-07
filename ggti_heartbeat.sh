
# GATEWAY WATCHDOG: MONITORING JNP-DIV-450K-2026-001
STATUS_CHECK=$(grep "GATEWAY_SUCCESS" $HOME/Jackson-Node/nodes/jackson_pharma_node/public_dispatch_feed.log)
if [ ! -z "$STATUS_CHECK" ]; then
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] | WATCHDOG: Checking transaction JNP-DIV-450K-2026-001 status..." >> $HOME/Jackson-Node/heartbeat.log
fi
STATUS_SOUTH_STREET=$(grep 'ACQUISITION' $HOME/Jackson-Node/nodes/south_street_node/south_street_ledger.log)
if [ ! -z "$STATUS_SOUTH_STREET" ]; then
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] | WATCHDOG: Monitoring South Street Acquisition..." >> $HOME/Jackson-Node/heartbeat.log
fi
