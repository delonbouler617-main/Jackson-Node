#!/usr/bin/env python3
import os
import subprocess

OUTPUT_DIR = os.path.expanduser("~/Jackson-Node/episodes/digital_world_ep1")
MP4_PATH = os.path.join(OUTPUT_DIR, "episode_1_telemetry.mp4")

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("==========================================================")
print(" GENERATING EPISODE 1 MP4 TELEMETRY STREAM")
print("==========================================================")

# Simple clean drawtext filter string escaping colons properly
filter_str = (
    "drawtext=text='DIGITAL WORLD EPISODE 1':x=50:y=50:fontsize=36:fontcolor=white,"
    "drawtext=text='DNHUAA TELEMETRY LOOP ACTIVE':x=50:y=100:fontsize=28:fontcolor=green,"
    "drawtext=text='RADAR SWEEP DEG':x=50:y=160:fontsize=24:fontcolor=yellow,"
    "drawtext=text='SUN ANGLE DEG':x=50:y=200:fontsize=24:fontcolor=cyan,"
    "drawtext=text='MOON ANGLE DEG':x=50:y=240:fontsize=24:fontcolor=magenta"
)

ffmpeg_cmd = [
    "ffmpeg", "-y",
    "-f", "lavfi",
    "-i", "testsrc=size=1280x720:rate=60",
    "-vf", filter_str,
    "-t", "10",
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    MP4_PATH
]

subprocess.run(ffmpeg_cmd, check=True)
print(f"\n[RENDER COMPLETE] MP4 compiled at: {MP4_PATH}")
