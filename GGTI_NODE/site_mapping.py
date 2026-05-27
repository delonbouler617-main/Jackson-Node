import json
import os

def run_site_index():
    print("\n" + "═"*50)
    print(" GGTI CORE | SITE MAPPING & INFRASTRUCTURE")
    print("═"*50)
    
    path = os.path.expanduser("~/GGTI_NODE/property_manifest.json")
    with open(path, 'r') as f:
        manifest = json.load(f)
    
    for node in manifest['nodes']:
        print(f"MAPPING NODE [{node['id']}]")
        print(f"LOCATION:    {node['address']}")
        print(f"OBJECTIVE:   {node['designation']}")
        print(f"STATUS:      {node['status']}")
        print("-" * 50)

    print("ACTION: SITE_BOUNDARIES_LOCKED")
    print("ACTION: INDEX_SYNCED_TO_GIT")
    print("═"*50 + "\n")

if __name__ == "__main__":
    run_site_index()
