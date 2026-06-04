import json
import os
import glob
from datetime import datetime

def launch_explorer():
    print("\n" + "="*50)
    print(" GGTI SOVEREIGN BLOCK EXPLORER | NODE: JACKSON-49203")
    print("="*50)
    
    node_path = os.path.expanduser("~/GGTI_NODE/*.json")
    files = glob.glob(node_path)
    
    if not files:
        print("NO DATA FOUND IN LEDGER.")
        return

    for file_path in files:
        filename = os.path.basename(file_path)
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        print(f"\n--- OBJECT: {filename} ---")
        for key, value in data.items():
            print(f"{key.upper()}: {value}")
        print("-" * 30)

    print("\n" + "="*50)
    print(f"QUERY COMPLETE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50 + "\n")

if __name__ == "__main__":
    launch_explorer()
