import json
import os

target = "+229 50798668"
log_file_path = "telephony_logs/flagged_registry.json"

print("\n=== GGTI TELEPHONY MONITOR SERVICE ===")
print(f"[MONITOR] Active Target Tracker: {target}")

if not os.path.exists(log_file_path):
    print("[ALERT] No baseline data registry found. Awaiting initial flag.")
else:
    match_count = 0
    latest_timestamp = "None"
    
    with open(log_file_path, "r") as f:
        for line in f:
            if line.strip():
                try:
                    entry = json.loads(line)
                    if entry.get("flagged_entity") == target:
                        match_count += 1
                        latest_timestamp = entry.get("timestamp", "Unknown")
                except json.JSONDecodeError:
                    continue
                    
    print(f"[STATS] Total Blocked Pings Cataloged: {match_count}")
    print(f"[STATS] Last Attempt Intercepted:      {latest_timestamp}")
    print("[STATUS] Perimeter Integrity: SECURE (Do Not Disturb Active)")
print("=======================================\n")
