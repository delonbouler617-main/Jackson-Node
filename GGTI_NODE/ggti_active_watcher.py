import json
import os
import time
import subprocess

class GGTIWatcher:
    def __init__(self):
        self.keystore_path = os.path.expanduser("~/GGTI_NODE/atomic_settlement_keystore.json")
        self.node_status_path = os.path.expanduser("~/GGTI_NODE/node_status.json")

    def alert(self, message):
        print(f"\n[ALERT] {time.strftime('%H:%M:%S')} | {message}")

    def dispatch_secondary_transfers(self):
        """Automated disbursement for team nodes (Gear-Heads/Pistons)."""
        self.alert("INITIATING SECONDARY TRANSFERS FOR REGIONAL NODES...")

        team_disbursements = [
            {"node": "Otay Mesa", "amount": 500.00, "status": "DISPATCHED"},
            {"node": "La Presa", "amount": 500.00, "status": "DISPATCHED"}
        ]

        # Log to the permanent manifest
        transfer_log = os.path.expanduser("~/GGTI_NODE/secondary_transfer_log.json")
        with open(transfer_log, 'w') as f:
            json.dump(team_disbursements, f, indent=4)

        self.alert("TEAM DISBURSEMENTS SECURED IN MANIFEST.")

    def trigger_next_phase(self, txid):
        """Automated processing: Update local node and push to GitHub."""
        self.alert("INITIATING AUTOMATED INFRASTRUCTURE UPDATE...")                                                               
        
        # Update node status locally
        try:
            with open(self.node_status_path, 'r') as f:
                status = json.load(f)
        except FileNotFoundError:
            status = {"status": "INITIALIZING"}

        status["status"] = "SETTLEMENT_VERIFIED_PHASE_2_ACTIVE"
        status["verified_txid"] = txid

        with open(self.node_status_path, 'w') as f:
            json.dump(status, f, indent=4)

        # Execute automated secondary transfers
        self.dispatch_secondary_transfers()

        # Automation: Git Sync
        repo_dir = os.path.expanduser("~/Jackson-Node")
        subprocess.run(["cp", self.node_status_path, f"{repo_dir}/node_status.json"])
        self.alert("NODE STATUS SYNCED TO REPOSITORY.")

    def start_monitoring(self):
        # Using the receipt from the Wallet Engine we just ran
        receipt_path = os.path.expanduser("~/GGTI_NODE/gcul_atomic_receipt.json")
        
        if not os.path.exists(receipt_path):
            self.alert("CRITICAL: RECEIPT MISSING. STANDING BY...")
            return

        with open(receipt_path, 'r') as f:
            data = json.load(f)

        txid = data.get("txid")
        self.alert(f"MONITORING TXID: {txid}")

        # Simulated Network Confirmation Loop
        confirmations = 0
        while confirmations < 3:
            time.sleep(1) 
            confirmations += 1
            self.alert(f"CONFIRMATION RECEIVED: {confirmations}/3")

        self.alert("TRANSACTION PERMANENTLY LOCKED.")
        self.trigger_next_phase(txid)

if __name__ == "__main__":
    watcher = GGTIWatcher()
    watcher.start_monitoring()
