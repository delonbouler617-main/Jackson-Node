import json
import os
import subprocess

def generate_ggti_token():
    """
    Protocol: Human-Machine Technical Archiving
    Generates a fresh OAuth2 token using the local gcloud environment.
    """
    try:
        # Pulls the token directly from your authenticated gcloud session
        token = subprocess.check_output(['gcloud', 'auth', 'print-access-token']).decode('utf-8').strip()
        return token
    except Exception:
        return None

def execute_atomic_settlement(asset_value):
    token = generate_ggti_token()
    if not token:
        print("Action Required: Please run 'gcloud auth login' first.")
        return

    manifest = {
        "txid": "0x9fd34b1a2e7699458d8b01067e08d689ebfa482bd9a195454918531d8f8dd2026",
        "value": asset_value,
        "protocol": "A2A_DIRECT",
        "logic": "ATOMIC_DISBURSEMENT",
        "auth_seal": "5178673216_MOTO_G_2026",
        "status": "POSITIVE_STATE_INITIATED"
    }

    path = os.path.expanduser("~/GGTI_NODE/settlement_0x9fd.json")
    with open(path, 'w') as f:
        json.dump(manifest, f, indent=2)

    print(f"BROADCASTING TO JACKSON-NODE-49203...")
    
    # Executing the curl broadcast using the freshly generated token
    broadcast_cmd = [
        "curl", "-X", "POST", "-s", "-o", "/dev/null", "-w", "%{http_code}",
        "-H", f"Authorization: Bearer {token}",
        "-H", "Content-Type: application/json",
        "-d", f"@{path}",
        "https://web3.googleapis.com/v1/projects/jackson-node-49203/locations/global/networks/blockchain/transactions:broadcast"
    ]
    
    try:
        response_code = subprocess.check_output(broadcast_cmd).decode('utf-8')
        if response_code == "200":
            print(f"SUCCESS: Settlement locked in ledger. Status: {response_code}")
        else:
            print(f"FAILURE: Gateway returned {response_code}. Potential 502/Auth issue.")
    except Exception as e:
        print(f"ERROR: Broadcast failed: {e}")

if __name__ == "__main__":
    execute_atomic_settlement("3150.00")
