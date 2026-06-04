import time, subprocess, os, json
from ggti_fleet_monitor import FleetMonitor
from ggti_blueprint_processor import BlueprintProcessor
from ggti_miner import GGTIMiner

def run_daemon():
    fleet = FleetMonitor()
    blueprints = BlueprintProcessor()
    miner = GGTIMiner(difficulty=5)
    node_path = os.path.expanduser("~/Jackson-Node")

    print("══ GGTI MASTER DAEMON: ONLINE ══")
    print("[*] TAX-VERIFIED LIQUIDITY MODE ACTIVE")

    while True:
        # 1. Structural Blueprint Check
        blueprints.process_new_assets()

        # 2. Mining & Tax Reconciliation
        # This solves the D5 puzzle and updates the spendable balance
        miner.update_ledger()

        # 3. Repository Sync
        try:
            subprocess.run(["git", "-C", node_path, "add", "."], check=True)
            subprocess.run(["git", "-C", node_path, "commit", "-m", "DAEMON_TAX_LIQUIDITY_SYNC"], capture_output=True)
            subprocess.run(["git", "-C", node_path, "push", "origin", "main"], capture_output=True)
            print(f"[*] {time.strftime('%H:%M:%S')} - GLOBAL RECONCILIATION COMPLETE")
        except Exception:
            print(f"[*] {time.strftime('%H:%M:%S')} - MODE: OFFLINE (Local Ledger Protected)")

        time.sleep(60)

if __name__ == "__main__":
    run_daemon()
