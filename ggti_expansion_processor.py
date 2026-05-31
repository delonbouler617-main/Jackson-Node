#!/usr/bin/env python3
import json
import os
import time

WALLET_LOG = os.path.expanduser("~/telephony_logs/wallet_balance_ledger.json")
EXPANSION_LOG = os.path.expanduser("~/telephony_logs/expansion_nodes.json")

def execute_expansion_purchase():
    if not os.path.exists(WALLET_LOG) or not os.path.exists(EXPANSION_LOG):
        print("[ERROR] Required ledger manifests are missing. Initialize assets first.")
        return

    # Load current wallet state
    with open(WALLET_LOG, "r") as f:
        wallet_data = json.load(f)

    # Load target expansion parameters
    with open(EXPANSION_LOG, "r") as f:
        expansion_data = json.load(f)

    # Tracking account identity bound to the physical device
    print(f"=== GGTI BATCH EXPANSION SUB-ENGINE ===")
    print(f"[ACCOUNT NODE] Active Core: {wallet_data.get('account_id')}")
    
    # Calculate initial balance in subunits to guarantee zero decimal drift
    current_bal_subunits = int(wallet_data["confirmed_balance"] * 100)
    print(f"[INITIAL BAL]  {wallet_data['confirmed_balance']} H.A.C")
    print("-" * 50)

    # Process batch transactions loop
    total_deduction_subunits = 0
    for node in expansion_data["nodes"]:
        gross_cost_subunits = node["financials_subunits"]["gross_settlement"]
        node_id = node["node_id"]
        
        print(f"[PROCESSING] Allocation Request for target: {node_id}")
        print(f"             Gross Subunits Staged: {gross_cost_subunits} (Price + Taxes + Fees)")
        
        total_deduction_subunits += gross_cost_subunits
        node["acquisition_status"] = "SETTLED_NODE_ACQUIRED"

    # Verify allocation threshold limits
    if current_bal_subunits >= total_deduction_subunits:
        new_bal_subunits = current_bal_subunits - total_deduction_subunits
        
        # Write updated parameters back to system states
        wallet_data["confirmed_balance"] = float(new_bal_subunits / 100)
        wallet_data["last_sync_timestamp"] = int(time.time())
        wallet_data["status"] = "EXPANSION_PACK_SETTLED"

        with open(WALLET_LOG, "w") as f:
            json.dump(wallet_data, f, indent=4)
        with open(EXPANSION_LOG, "w") as f:
            json.dump(expansion_data, f, indent=4)

        print("-" * 50)
        print(f"[BATCH SUCCESS] Deducted total of {total_deduction_subunits / 100} H.A.C")
        print(f"[FINAL BALANCE] Updated Ledger State: {wallet_data['confirmed_balance']} H.A.C")
        print(f"[STATUS]        Hupp Ave & Mitchell Nodes Status set to: SETTLED_NODE_ACQUIRED")
    else:
        print("[ERROR] Insufficient ledger allocation units to clear physical land parcel bounds.")

if __name__ == "__main__":
    execute_expansion_purchase()
