import os
import json
import subprocess

class GGTI_Backend:
    def __init__(self):
        self.node_id = "jackson-node-49203"
        self.root_dir = os.path.expanduser("~/GGTI_NODE")
        self.config_path = os.path.join(self.root_dir, "config.json")
        
        if not os.path.exists(self.root_dir):
            os.makedirs(self.root_dir)

    def initialize_state(self):
        """Sets the system to POSITIVE_STATE_INITIATED."""
        state = {
            "status": "ACTIVE",
            "protocol": "GGTI_CORE_V1",
            "hardware_seal": "MOTO_G_2026_ANDROID_16",
            "node_origin": "Jackson_Michigan_49203"
        }
        with open(self.config_path, 'w') as f:
            json.dump(state, f, indent=4)
        return "NODE_READY: POSITIVE_STATE_INITIATED"

if __name__ == "__main__":
    node = GGTI_Backend()
    print(node.initialize_state())
