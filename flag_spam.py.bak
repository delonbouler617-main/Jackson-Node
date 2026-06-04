import json
import os
from datetime import datetime

# Define the spam profile metadata
target_number = "+229 50798668"
origin_country = "Benin (West Africa)"
threat_type = "Persistent Telephony Spam"

log_entry = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "flagged_entity": target_number,
    "origin_zone": origin_country,
    "classification": threat_type,
    "status": "FLAGGED_IN_DATABASE"
}

# Ensure log directory exists
os.makedirs("telephony_logs", exist_ok=True)

# Append to local iSH audit file
with open("telephony_logs/flagged_registry.json", "a") as f:
    f.write(json.dumps(log_entry) + "\n")

print(f"\n=== iSH TERMINAL REGISTRY FLAG ===")
print(f"[FLAGGED] Target: {target_number}")
print(f"[ROUTING] Origin: {origin_country}")
print(f"[STATUS]  Successfully recorded to local repository log.")
