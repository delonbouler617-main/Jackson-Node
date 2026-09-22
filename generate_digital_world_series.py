#!/usr/bin/env python3
import os
import sys
import subprocess
import numpy as np

# Engine Detection & Auto-Fallback Protocol
ENGINE = None
try:
    import cv2
    ENGINE = "OPENCV"
    print("[SYSTEM INFO] Primary Engine Loaded: OpenCV (cv2)")
except ImportError:
    try:
        from PIL import Image, ImageDraw
        ENGINE = "PILLOW"
        print("[SYSTEM INFO] Backup Engine Loaded: Pillow (PIL)")
    except ImportError:
        print("[FATAL ERROR] Neither OpenCV nor Pillow available!")
        sys.exit(1)

OUTPUT_DIR = os.path.expanduser("~/Jackson-Node/episodes")
EPISODE_COUNT = 10
DURATION_PER_EP_SEC = 900  # 15 Minutes
FPS = 15
WIDTH, HEIGHT = 1280, 720

EPISODE_TITLES = {
    1: "CHASSIS FABRICATION & TELEMETRY INIT",
    2: "ARMOR PLATING & TURRET ASSEMBLY",
    3: "ENGINE IGNITION & FIELD TACTICS",
    4: "DEPLOYMENT TO DIGITAL NODE 1",
    5: "TARGET LOCK & RADAR RANGEFINDING",
    6: "ENGAGING FIRST ENEMY FORTIFICATION",
    7: "TARGET 1 DESTROYED & IMPACT ANALYTICS",
    8: "COUNTER-MEASURES & DEFENSIVE BARRIER",
    9: "ADVANCING TO SECTOR B TARGETS",
    10: "FULL SWEEP CLEARANCE & SATELLITE LINK"
}

os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_frame_opencv(episode_num, frame_index):
    img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    bar_width = WIDTH // 7
    colors = [
        (255, 255, 255), (0, 255, 255), (255, 255, 0), (0, 255, 0),
        (255, 0, 255), (0, 0, 255), (255, 0, 0)
    ]
    for i in range(7):
        img[:, i*bar_width:(i+1)*bar_width] = colors[i]

    center_x, center_y = WIDTH // 2, HEIGHT // 2
    cv2.circle(img, (center_x, center_y), 280, (0, 0, 200), -1)

    time_sec = frame_index / FPS
    radar_angle = int((time_sec * 30) % 360)
    sun_angle = int((time_sec * 2) % 360)
    moon_angle = int((180 + time_sec * 1.5) % 360)

    ep_title = EPISODE_TITLES.get(episode_num, "OPERATIONAL")
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.rectangle(img, (0, 0), (WIDTH, 140), (0, 0, 0), -1)
    cv2.putText(img, f"DIGITAL WORLD EPISODE {episode_num}: {ep_title}", (30, 40), font, 0.9, (255, 255, 255), 2)
    cv2.putText(img, f"DNHUAA TELEMETRY LOOP : ACTIVE [{int(time_sec)}s / {DURATION_PER_EP_SEC}s]", (30, 80), font, 0.7, (0, 255, 0), 2)

    cv2.putText(img, f"RADAR SWEEP : {radar_angle} DEG", (30, 200), font, 0.8, (0, 255, 255), 2)
    cv2.putText(img, f"SUN ANG     : {sun_angle} DEG", (30, 240), font, 0.8, (0, 255, 255), 2)
    cv2.putText(img, f"MOON ANGLE  : {moon_angle} DEG", (30, 280), font, 0.8, (0, 255, 255), 2)

    target_dist = max(10, 1500 - int(time_sec * 1.5))
    cv2.rectangle(img, (WIDTH - 400, HEIGHT - 220), (WIDTH - 40, HEIGHT - 40), (0, 0, 0), -1)
    cv2.rectangle(img, (WIDTH - 400, HEIGHT - 220), (WIDTH - 40, HEIGHT - 40), (0, 255, 0), 2)
    cv2.putText(img, "TANK OPERATIONAL STATUS", (WIDTH - 380, HEIGHT - 180), font, 0.6, (255, 255, 255), 1)
    cv2.putText(img, f"TARGET DIST : {target_dist}M", (WIDTH - 380, HEIGHT - 140), font, 0.6, (0, 255, 0), 2)

    if episode_num >= 7:
        cv2.putText(img, "TARGET 1 : DESTROYED", (WIDTH - 380, HEIGHT - 100), font, 0.6, (0, 0, 255), 2)
    else:
        cv2.putText(img, "TARGET 1 : ACQUIRING", (WIDTH - 380, HEIGHT - 100), font, 0.6, (0, 255, 255), 2)

    scan_y = int((frame_index * 8) % HEIGHT)
    cv2.line(img, (0, scan_y), (WIDTH, scan_y), (255, 0, 255), 3)

    return img.tobytes(), 'bgr24'

def generate_frame_pillow(episode_num, frame_index):
    from PIL import Image, ImageDraw
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)

    bar_width = WIDTH // 7
    colors = [
        (255, 255, 255), (255, 255, 0), (0, 255, 255), (0, 255, 0),
        (255, 0, 255), (255, 0, 0), (0, 0, 255)
    ]
    for i in range(7):
        draw.rectangle([i * bar_width, 0, (i + 1) * bar_width, HEIGHT], fill=colors[i])

    center_x, center_y = WIDTH // 2, HEIGHT // 2
    draw.ellipse([center_x - 280, center_y - 280, center_x + 280, center_y + 280], fill=(200, 0, 0))

    time_sec = frame_index / FPS
    radar_angle = int((time_sec * 30) % 360)
    sun_angle = int((time_sec * 2) % 360)
    moon_angle = int((180 + time_sec * 1.5) % 360)
    ep_title = EPISODE_TITLES.get(episode_num, "OPERATIONAL")

    draw.rectangle([0, 0, WIDTH, 140], fill=(0, 0, 0))
    draw.text((30, 20), f"DIGITAL WORLD EPISODE {episode_num}: {ep_title}", fill=(255, 255, 255))
    draw.text((30, 60), f"DNHUAA TELEMETRY LOOP : ACTIVE [{int(time_sec)}s / {DURATION_PER_EP_SEC}s]", fill=(0, 255, 0))

    draw.text((30, 180), f"RADAR SWEEP : {radar_angle} DEG", fill=(0, 255, 255))
    draw.text((30, 220), f"SUN ANG     : {sun_angle} DEG", fill=(0, 255, 255))
    draw.text((30, 260), f"MOON ANGLE  : {moon_angle} DEG", fill=(0, 255, 255))

    target_dist = max(10, 1500 - int(time_sec * 1.5))
    draw.rectangle([WIDTH - 400, HEIGHT - 220, WIDTH - 40, HEIGHT - 40], fill=(0, 0, 0), outline=(0, 255, 0))
    draw.text((WIDTH - 380, HEIGHT - 200), "TANK OPERATIONAL STATUS", fill=(255, 255, 255))
    draw.text((WIDTH - 380, HEIGHT - 160), f"TARGET DIST : {target_dist}M", fill=(0, 255, 0))

    if episode_num >= 7:
        draw.text((WIDTH - 380, HEIGHT - 120), "TARGET 1 : DESTROYED", fill=(255, 0, 0))
    else:
        draw.text((WIDTH - 380, HEIGHT - 120), "TARGET 1 : ACQUIRING", fill=(0, 255, 255))

    scan_y = int((frame_index * 8) % HEIGHT)
    draw.line([(0, scan_y), (WIDTH, scan_y)], fill=(255, 0, 255), width=3)

    return np.array(img).tobytes(), 'rgb24'

def render_episode(ep_num):
    ep_dir = os.path.join(OUTPUT_DIR, f"digital_world_ep{ep_num}")
    os.makedirs(ep_dir, exist_ok=True)
    output_path = os.path.join(ep_dir, f"episode_{ep_num}_telemetry.mp4")

    pix_fmt = 'bgr24' if ENGINE == "OPENCV" else 'rgb24'
    total_frames = DURATION_PER_EP_SEC * FPS

    ffmpeg_cmd = [
        'ffmpeg', '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-s', f'{WIDTH}x{HEIGHT}',
        '-pix_fmt', pix_fmt,
        '-r', str(FPS),
        '-i', '-',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast',
        '-crf', '28',
        output_path
    ]

    print(f"\n[+] Starting Render: Episode {ep_num} / {EPISODE_COUNT} using [{ENGINE}]...")
    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    try:
        for f in range(total_frames):
            if ENGINE == "OPENCV":
                frame_bytes, _ = generate_frame_opencv(ep_num, f)
            else:
                frame_bytes, _ = generate_frame_pillow(ep_num, f)

            proc.stdin.write(frame_bytes)

            if f % (FPS * 60) == 0:
                mins_done = f // (FPS * 60)
                print(f"    Progress: {mins_done} / 15 Minutes rendered...")

        proc.stdin.close()
        proc.wait()
        print(f"[✓] Episode {ep_num} Complete: {output_path}")

    except Exception as e:
        print(f"[!] Error during rendering Episode {ep_num}: {e}")
        proc.kill()

def main():
    for ep in range(1, EPISODE_COUNT + 1):
        render_episode(ep)
    print("\n[★] Operation Complete: All Episodes Generated cleanly.")

if __name__ == "__main__":
    main()
