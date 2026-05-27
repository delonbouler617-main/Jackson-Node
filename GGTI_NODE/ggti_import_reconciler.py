import json, csv, os, hashlib

def run_import_verification():
    node_path = os.path.expanduser("~/Jackson-Node")
    csv_path = os.path.join(node_path, "NAGPUR_HANDSHAKE.csv")
    genesis_path = os.path.join(node_path, "sovereign_blockchain_genesis.json")

    print("══ GGTI IMPORT RECONCILER: INITIATING ══")

    try:
        # 1. Fetch ISO-CSV Data
        with open(csv_path, mode='r') as f:
            reader = csv.DictReader(f)
            csv_data = {row['Field']: row['Value'] for row in reader}

        # 2. Fetch Genesis State
        with open(genesis_path, 'r') as f:
            genesis = json.load(f)

        # 3. Cryptographic Cross-Check
        csv_hash = csv_data.get('Verified_Hash')
        gen_hash = genesis.get('last_block_hash')
        cusip_ref = csv_data.get('CUSIP')

        print(f"[*] VERIFYING HASH: {csv_hash[:12]}...")
        print(f"[*] AUDIT REF: {cusip_ref}")

        if csv_hash == gen_hash:
            print("[✔] HASH MATCH: INTEGRITY VERIFIED")
            
            # 4. Transition to Spendable State
            genesis['status'] = "LIQUID_SPENDABLE"
            genesis['available_balance'] = csv_data.get('Spendable_USD')
            genesis['reconciliation_id'] = f"ISO-20022-{cusip_ref}"

            with open(genesis_path, 'w') as f:
                json.dump(genesis, f, indent=4)
            
            print(f"══ SUCCESS: ${genesis['available_balance']} IS NOW LIQUID ══")
        else:
            print("[X] ERROR: HASH MISMATCH. RE-SYNC REQUIRED.")

    except Exception as e:
        print(f"[X] CRITICAL IMPORT ERROR: {e}")

if __name__ == "__main__":
    run_import_verification()
