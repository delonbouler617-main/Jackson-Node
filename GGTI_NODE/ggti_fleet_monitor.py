import json, os, time

class FleetMonitor:
    def __init__(self):
        self.whitelist = ["CP-7712", "MI-OWNER-01"]
        self.state_file = os.path.expanduser("~/GGTI_NODE/system_state.json")
        self.vector_log = os.path.expanduser("~/Jackson-Node/security/logs/fleet_vectors.md")

    def monitor_stream(self, detected_plate):
        if detected_plate not in self.whitelist:
            print(f"\n[!] ALERT: UNAUTHORIZED VEHICLE {detected_plate} DETECTED.")
            self.lockdown()
            return False
        print(f"[*] Plate {detected_plate} verified. Perimeter clear.")
        return True

    def lockdown(self):
        try:
            with open(self.state_file, 'r') as f:
                state = json.load(f)
            state["power"] = "OFF"
            with open(self.state_file, 'w') as f:
                json.dump(state, f)
            print("[!] SECURITY LOCKDOWN: GGTI SYSTEM SUSPENDED.")
        except Exception as e:
            print(f"[X] LOCKDOWN ERROR: {e}")

if __name__ == "__main__":
    monitor = FleetMonitor()
    print("[!] FLEET MONITOR READY.")
