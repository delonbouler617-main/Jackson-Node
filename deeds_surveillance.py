import requests
import time
from datetime import datetime

# GGTI NODE TARGETS
NODES = ["409 HUPP AVE", "429 HUPP AVE", "MITCHELL ST"]
SLEEP_INTERVAL = 900  # 15-minute pulse frequency

def check_registry():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] GGTI HANDSHAKE: PINGING JACKSON COUNTY...")
    portal_url = "https://bsaonline.com/Home/Index?uid=388"
    try:
        response = requests.get(portal_url, timeout=15)
        if response.status_code == 200:
            # Registry Node is alive. 
            # Note: Phase 1 ignition requires the physical seal confirmation via fax handshake.
            return False 
        return False
    except Exception as e:
        print(f"ERROR: Handshake packet dropped. {e}")
        return False

print("GGTI SURVEILLANCE NODE: INITIALIZED.")
while True:
    if check_registry():
        print("\n[!!!] ZENITH ALERT: RECORDING DETECTED [!!!]")
        break
    else:
        print("STATE: NO NEW PACKETS. Monitoring registry queue...")
        time.sleep(SLEEP_INTERVAL)
