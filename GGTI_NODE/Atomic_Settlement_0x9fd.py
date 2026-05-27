import json
import os

def execute_atomic_settlement(asset_value):
    manifest = {
        "txid": "0x9fd34b1a2e7699458d8b01067e08d689ebfa482bd9a195454918531d8f8dd2026",
        "value": asset_value,
        "protocol": "A2A_DIRECT",
        "logic": "ATOMIC_DISBURSEMENT",
        "auth_seal": "5178673216_MOTO_G_2026",
        "status": "POSITIVE_STATE_INITIATED"
    }
    
    # Ensure directory exists
    os.makedirs(os.path.expanduser("~/GGTI_NODE"), exist_ok=True)
    
    # Output to local JSON for the curl broadcast
    path = os.path.expanduser("~/GGTI_NODE/settlement_0x9fd.json")
    with open(path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"SUCCESS: Local manifest generated at {path}")
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    execute_atomic_settlement("3150.00")
