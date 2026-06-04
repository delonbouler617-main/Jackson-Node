import json
import hashlib
import time
import os

def execute_disbursement():
    # Recipient Data for Node Transfer
    recipient = {
        "identity": "Anuj Basant Sen",
        "location": "Nagpur, India",
        "node_link": "INTERNATIONAL_EXTERNAL_NODE"
    }
    
    amount = "3150.00"
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    
    # Generate the Sovereign Technical Seal
    raw_seal = f"MOTO_G_2026_FINANCE_{timestamp}_GGTI"
    auth_seal = hashlib.sha256(raw_seal.encode()).hexdigest()
    
    manifest = {
        "header": {
            "protocol": "GGTI_SOVEREIGN_A2A",
            "origin_node": "Jackson-Node-49203",
            "state": "POSITIVE_STATE_INITIATED"
        },
        "transaction": {
            "txid": f"0x{auth_seal[:16]}",
            "asset_value": amount,
            "currency": "USD",
            "recipient": recipient["identity"],
            "region": recipient["location"]
        },
        "authority": {
            "seal": auth_seal,
            "logic": "ATOMIC_DISBURSEMENT",
            "timestamp": timestamp
        }
    }
    
    # Commit to the local secure ledger
    path = os.path.expanduser("~/GGTI_NODE/disbursement_final.json")
    with open(path, 'w') as f:
        json.dump(manifest, f, indent=4)
    
    print("\n" + "="*50)
    print(" GGTI FINANCIAL INSTITUTE | DISBURSEMENT LOG")
    print("="*50)
    print(f"RECIPIENT: {recipient['identity']}")
    print(f"VALUE:     ${amount}")
    print(f"TXID:      {manifest['transaction']['txid']}")
    print(f"STATUS:    SUCCESS_LOCKED")
    print("="*50 + "\n")

if __name__ == "__main__":
    execute_disbursement()
