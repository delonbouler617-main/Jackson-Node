import time
import signal
import sys
import json
import os

class GGTIGovernance:
    def __init__(self):
        self.system_active = True
        self.node_id = "MOTO_G_2026_MASTER"
        # Registering the "Off Switch" (SIGINT/Ctrl+C)
        signal.signal(signal.signal.SIGINT, self.emergency_shutdown)

    def alert_led(self, status):
        color = "🟢 [ON]" if status else "🔴 [OFF]"
        print(f"\r{time.strftime('%H:%M:%S')} | LED STATUS: {color} | NODE: {self.node_id}", end="")

    def emergency_shutdown(self, signum, frame):
        """The 'Off Switch' logic for the SSH/Terminal."""
        print("\n\n[!] MASTER SWITCH FLIPPED: OFF")
        self.system_active = False
        self.lock_ledger()
        print("[!] ALL GGTI NODES DISCONNECTED. SHUTDOWN COMPLETE.")
        sys.exit(0)

    def lock_ledger(self):
        """Final action before power-down."""
        print("[!] LOCKING GCUL ATOMIC LEDGER...")
        time.sleep(1)

    def run_sync(self):
        print("══ GGTI AUTHORIZED LED OPERATIONAL SYNC INITIATED ══")
        print("Press Ctrl+C to flip the Master Switch to OFF.")
        try:
            while self.system_active:
                self.alert_led(True)
                time.sleep(0.5)
        except Exception as e:
            self.emergency_shutdown(None, None)

if __name__ == "__main__":
    gov = GGTIGovernance()
    gov.run_sync()
