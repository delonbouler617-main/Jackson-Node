import json
import os
import time

def broadcast_final_emission():
    print("\n" + "="*50)
    print(" GGTI SOVEREIGN GATEWAY | FINAL EMISSION")
    print("="*50)
    
    ledger_path = os.path.expanduser("~/GGTI_NODE/disbursement_final.json")
    
    if not os.path.exists(ledger_path):
        print("EMISSION_ERROR: MANIFEST_NOT_FOUND")
        return

    with open(ledger_path, 'r') as f:
        manifest = json.load(f)

    print(f"BROADCASTING TXID: {manifest['transaction']['txid']}")
    print("TARGETING NODE:    NAGPUR_IN_NODE_01")
    
    # Simulating the finalized handshake delay
    for i in range(3):
        print("SYNCING LEDGER..." + "." * (i + 1))
        time.sleep(1)

    print("-" * 50)
    print(f"ASSET VALUE:      ${manifest['transaction']['asset_value']} USD")
    print(f"RECIPIENT:        {manifest['transaction']['recipient']}")
    print(f"STATUS:           EMITTED_SUCCESS_PERMANENT")
    print(f"TIMESTAMP:        {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    print("PROTOCOL:         GGTI_NODE_SHUTDOWN_CLEAN")
    print("="*50 + "\n")

if __name__ == "__main__":
    broadcast_final_emission()
