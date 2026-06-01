#!/usr/bin/env python3
import json
import os
import time

WALLET_LOG = os.path.expanduser("~/telephony_logs/wallet_balance_ledger.json")
CRYPTO_LOG = os.path.expanduser("~/telephony_logs/crypto_outbound_manifest.json")

def process_crypto_allocation():
    if not os.path.exists(WALLET_LOG):
        print("[ERROR] Core balance ledger target file cannot be located.")
        return

    with open(WALLET_LOG, "r") as f:
        wallet_data = json.load(f)

    # Fixed-point safety validation
    current_subunits = int(wallet_data["confirmed_balance"] * 100)
    deduction_subunits = 15000  # Exact $150.00 mapping (15,000 cents)

    if current_subunits >= deduction_subunits:
        new_subunits = current_subunits - deduction_subunits
        wallet_data["confirmed_balance"] = float(new_subunits / 100)
        wallet_data["last_sync_timestamp"] = int(time.time())
        wallet_data["status"] = "OUTBOUND_CRYPTO_ALLOCATION_SETTLED"

        # Construct the outbound transaction manifest profile
        tx_manifest = {
            "network": "Ethereum (ETH)",
            "target_address": "0x0a99A4e48DA8B35175b52EAC7B3154B3d13aBE98",
            "amount_usd_equivalent": 150.00,
            "amount_subunits": deduction_subunits,
            "timestamp_epoch": int(time.time()),
            "status": "STAGED_FOR_BROADCAST"
        }

        # Write updates back to local database layers
        with open(WALLET_LOG, "w") as f:
            json.dump(wallet_data, f, indent=4)
        with open(CRYPTO_LOG, "w") as f:
            json.dump(tx_manifest, f, indent=4)

        print("=== GGTI CRYPTO OUTBOUND MAPPING ===")
        print(f"[IDENTITY MASTER] : Melammu-Strike-70")
        print(f"[TARGET NETWORK]  : {tx_manifest['network']}")
        print(f"[DESTINATION ADDR]: {tx_manifest['target_address']}")
        print(f"[DEDUCTION UNITS] : -150.00 H.A.C")
        print(f"[UPDATED BALANCE] : {wallet_data['confirmed_balance']} H.A.C")
        print("====================================")
    else:
        print(f"[ERROR] Insufficient core ledger funds. Current balance: {wallet_data['confirmed_balance']} H.A.C")

if __name__ == "__main__":
    process_crypto_allocation()
