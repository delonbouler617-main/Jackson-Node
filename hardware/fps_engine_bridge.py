#!/usr/bin/env python3
import os
import json
import time
from datetime import datetime

MANIFEST_PATH = os.path.expanduser("~/Jackson-Node/episodes/digital_world_ep1/episode_1_manifest.json")

def load_manifest():
    if os.path.exists(MANIFEST_PATH):
        with open(MANIFEST_PATH, 'r') as f:
            return json.load(f)
    return {"status": "UNKNOWN"}

def run_fps_loop():
    print("==========================================================")
    print(" DIGITAL WORLD: FPS ENGINE + DNHUAA SUN/MOON BRIDGE")
    print("==========================================================")

    manifest = load_manifest()
    episode_title = manifest.get("episode", {}).get("title", "Digital World")
    ep_num = manifest.get("episode", {}).get("episode_number", 1)
    telemetry_type = manifest.get("episode", {}).get("telemetry", {}).get("celestial_engine", "UNKNOWN")

    print(f"[ENGINE LINK] Episode {ep_num}: {episode_title}")
    print(f"[ENGINE LINK] Telemetry Engine: {telemetry_type}")
    print("[ENGINE LINK] Streaming real-time telemetry loop (60 FPS tick)...")
    print("----------------------------------------------------------")

    frame = 0
    try:
        while True:
            frame += 1
            # Real-time radar sweep angle (0° - 360°)
            radar_angle = (frame * 6) % 360
            
            # Sun & Moon orbital telemetry calculation
            sun_angle = (frame * 0.25) % 360.0
            moon_angle = (sun_angle + 180.0) % 360.0
            
            # Formatted live telemetry output
            status_line = (
                f"\r[FRAME {frame:06d}] RADAR: {radar_angle:03d}° | "
                f"SUN: {sun_angle:06.2f}° | MOON: {moon_angle:06.2f}° | "
                f"DNHUAA: ACTIVE"
            )
            print(status_line, end="", flush=True)
            time.sleep(1 / 60)
    except KeyboardInterrupt:
        print("\n\n[ENGINE LINK] Bridge terminated safely.")

if __name__ == "__main__":
    run_fps_loop()
