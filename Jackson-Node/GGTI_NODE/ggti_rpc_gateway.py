from web3 import Web3
import json
import os
import time

def initialize_external_bridge():
    print("\n" + "="*50)
    print(" GGTI WEB3 RPC GATEWAY | EXTERNAL NETWORK BRIDGE")
    print("="*50)
    
    # Connecting to a public Ethereum RPC endpoint
    rpc_url = "https://rpc.ankr.com/eth"
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    if w3.is_connected():
        print("NETWORK STATUS:   POSITIVE_STATE_CONNECTED")
        print(f"CURRENT BLOCK:    {w3.eth.block_number}")
    else:
        print("NETWORK STATUS:   OFFLINE_AWAITING_CONNECTION")
        return

    # Load the Sovereign Manifest
    ledger_path = os.path.expanduser("~/GGTI_NODE/disbursement_final.json")
    if not os.path.exists(ledger_path):
        print("MANIFEST STATUS:  NOT_FOUND")
        return
        
    with open(ledger_path, 'r') as f:
        manifest = json.load(f)
        
    amount = manifest['transaction']['asset_value']
    txid = manifest['transaction']['txid']
    
    print("-" * 50)
    print(" PREPARING PAYLOAD FOR BROADCAST")
    print("-" * 50)
    print(f"ASSET VALUE:      ${amount}")
    print(f"INTERNAL TXID:    {txid}")
    print(f"TARGET IDENTITY:  {manifest['transaction']['recipient']}")
    print("-" * 50)
    print("AWAITING RECIPIENT PUBLIC WALLET ADDRESS (0x...)")
    print("="*50 + "\n")

if __name__ == "__main__":
    initialize_external_bridge()
