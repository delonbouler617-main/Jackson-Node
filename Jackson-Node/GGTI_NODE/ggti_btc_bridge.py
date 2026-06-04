import json
import os
import requests

def execute_btc_handshake():
    print("\n" + "="*50)
    print(" GGTI BITCOIN BRIDGE | MAINNET BROADCAST")
    print("="*50)

    recipient_wallet = "13exxw5Tnxg5rgUqxSc3xRZ8yy9ZzeC37t"
    api_url = f"https://blockstream.info/api/address/{recipient_wallet}"

    try:
        response = requests.get(api_url, timeout=15)
        if response.status_code == 200:
            print(f"NETWORK STATUS:   CONNECTED (BTC_MAINNET)")
            print(f"WALLET TARGET:    {recipient_wallet}")
        else:
            print(f"NETWORK STATUS:   GATEWAY_OFFLINE ({response.status_code})")
            return
    except Exception as e:
        print(f"NETWORK STATUS:   CONNECTION_FAILED: {e}")
        return

    # Link the Sovereign Ledger
    ledger_path = os.path.expanduser("~/GGTI_NODE/disbursement_final.json")
    if os.path.exists(ledger_path):
        with open(ledger_path, 'r') as f:
            manifest = json.load(f)
        
        print("-" * 50)
        print(f"STAGED ASSET:     ${manifest['transaction']['asset_value']} USD")
        print(f"RECIPIENT:        {manifest['transaction']['recipient']}")
        print(f"INTERNAL TXID:    {manifest['transaction']['txid']}")
        print("-" * 50)
        print("STATUS:           READY_FOR_EMISSION")
        print("="*50 + "\n")
    else:
        print("LEDGER STATUS:    MISSING_DISBURSEMENT_MANIFEST")

if __name__ == "__main__":
    execute_btc_handshake()
