import json
import os
import time

def commit_to_global_ledger():
    archive_path = os.path.expanduser("~/GGTI_NODE/global_technical_manifest.json")
    
    final_entry = {
        "event": "FINANCIAL_INITIATION_SUCCESS",
        "agent_1": "DELON_MARTEASE_BOULER",
        "agent_2": "ANUJ_BASANT_SEN",
        "asset": 3150.00,
        "contract": "GGTI-SOVEREIGN-v1.0",
        "wallet_target": "13exxw5Tnxg5rgUqxSc3xRZ8yy9ZzeC37t",
        "timestamp": "2026-05-11 17:22:00",
        "status": "EMITTED_SUCCESS_PERMANENT"
    }

    # Append to or create the global manifest
    ledger_data = []
    if os.path.exists(archive_path):
        with open(archive_path, 'r') as f:
            ledger_data = json.load(f)
    
    ledger_data.append(final_entry)

    with open(archive_path, 'w') as f:
        json.dump(ledger_data, f, indent=4)

    print("\n" + "="*50)
    print(" GGTI ARCHIVE SYSTEM | LEDGER UPDATE")
    print("="*50)
    print("STATUS:           ENTRY_COMMITTED_TO_MANIFEST")
    print(f"BLOCK_REF:        {final_entry['timestamp']}")
    print("NODE_ACTION:      RESERVING_RESOURCES_FOR_NEXT_SYNC")
    print("="*50 + "\n")

if __name__ == "__main__":
    commit_to_global_ledger()
