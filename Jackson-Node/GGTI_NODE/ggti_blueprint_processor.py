import os, json, time

class BlueprintProcessor:
    def __init__(self):
        self.draft_dir = os.path.expanduser("~/Jackson-Node/RENOVATION_DRAFTS")
        self.manifest_path = os.path.join(self.draft_dir, "mitchell_tower_manifest.md")

    def process_new_assets(self):
        """Indexes new drafts and prepares metadata for 3D processing."""
        files = [f for f in os.listdir(self.draft_dir) if f.endswith(('.jpg', '.png', '.pdf'))]
        if not files:
            return

        print(f"[*] {len(files)} STRUCTURAL ASSETS DETECTED. INDEXING...")
        with open(self.manifest_path, "a") as m:
            for f in files:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                m.write(f"\n- **Asset:** {f} | **Timestamp:** {timestamp} | **Status:** STAGED_FOR_RENDER")
        
        print("[✔] MITCHELL TOWER MANIFEST UPDATED.")

if __name__ == "__main__":
    processor = BlueprintProcessor()
    processor.process_new_assets()
