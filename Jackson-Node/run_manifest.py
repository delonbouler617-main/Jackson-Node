import hashlib
import json
import os

# 1. Define the raw data array from the manifest
routing_number = "071012344"
account_number = "700112345652"
transaction_id = "TXN0001"

# 2. Compute the exact SHA-256 Security Hash of the concatenated payload
concat_payload = f"{routing_number}{account_number}{transaction_id}"
security_hash = hashlib.sha256(concat_payload.encode('utf-8')).hexdigest()

# 3. Structure the finalized render output
manifest_data = {
    "routing_track": routing_number,
    "account_track": account_number,
    "transaction_id": transaction_id,
    "security_hash_sha256": security_hash,
    "status": "PRODUCTION_LOCKED"
}

print("\n=== GGTI MANIFEST VALIDATION RENDER ===")
print(f"[STATUS] ROUTING: {routing_number}")
print(f"[STATUS] ACCOUNT: {account_number}")
print(f"[STATUS] HASH:    {security_hash}")

# 4. Save the entry to the permanent ledger audit trail
os.makedirs("manifests", exist_ok=True)
with open("manifests/ledger_audit_trail.txt", "a") as log_file:
    log_file.write(json.dumps(manifest_data) + "\n")

print("[SUCCESS] Data structure permanently anchored to local ledger.\n")
