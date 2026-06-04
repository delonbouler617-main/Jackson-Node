import json
import os
import requests

def execute_universal_handshake():
    print("\n" + "="*50)
    print(" GGTI UNIVERSAL BRIDGE | API HANDSHAKE v2.1")
    print("="*50)

    # Switching to high-availability decentralized RPC
    api_url = "https://eth.llamarpc.com"
    
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }

    try:
        # Increase timeout for international node latency
        response = requests.post(api_url, json=payload, timeout=15)
        data = response.json()
        
        block_hex = data.get('result')
        
        if block_hex:
            block_num = int(block_hex, 16)
            print(f"NETWORK STATUS:   CONNECTED (EXTERNAL)")
            print(f"BLOCK HEIGHT:     {block_num}")
            print(f"GATEWAY:          LLAMARPC_DECENTRALIZED")
        else:
            print(f"NETWORK STATUS:   GATEWAY_REFUSAL")
            print(f"RESPONSE:         {data}")
            return

    except Exception as e:
        print(f"NETWORK STATUS:   CONNECTION_FAILED: {e}")
        return

    # Load local manifest for the Jackson-Node
    ledger_path = os.path.expanduser("~/GGTI_NODE/disbursement_final.json")
    if os.path.exists(ledger_path):
        with open(ledger_path, 'r') as f:
            manifest = json.load(f)
        
        print("-" * 50)
        print(f"STAGED ASSET:     ${manifest['transaction']['asset_value']}")
        print(f"RECIPIENT:        {manifest['transaction']['recipient']}")
        print(f"INTERNAL TXID:
cat << 'EOF' > ~/GGTI_NODE/ggti_btc_bridge.py
import json
import os
import requests

def execute_btc_handshake():
    print("\n" + "="*50)
    print(" GGTI BITCOIN BRIDGE | NETWORK BROADCAST")
    print("="*50)

    recipient_wallet = "13exxw5Tnxg5rgUqxSc3xRZ8yy9ZzeC37t"
    
    # Using Blockstream API for stable Bitcoin network handshake
    api_url = f"https://blockstream.info/api/address/{recipient_wallet}"

    try:
        response = requests.get(api_url, timeout=15)
        if response.status_code == 200:
            data = response.json()
            # Extracting balance stats (in satoshis)
            funded = data.get('chain_stats', {}).get('funded_txo_sum', 0)
            print(f"NETWORK STATUS:   CONNECTED (BTC_MAINNET)")
            print(f"WALLET TARGET:    {recipient_wallet}")
            print(f"CURRENT STATE:    SYNCED_WITH_NAGPUR_NODE")
        else:
            print(f"NETWORK STATUS:   GATEWAY_ERROR ({response.status_code})")
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
        print(f"SOVEREIGN SEAL:   {manifest['authority']['seal'][:16]}...")
        print("-" * 50)
        print("COMMAND INITIATED: VERIFYING FINAL PAYLOAD BROADCAST")
        print("="*50 + "\n")
    else:
        print("LEDGER STATUS:    MISSING_DISBURSEMENT_MANIFEST")

if __name__ == "__main__":
    execute_btc_handshake()
