#!/usr/bin/env python3
"""
Optimize images under assets/images for web delivery.

This script:
- Backs up originals to `assets/images/original-backups/`.
- Resizes images down to max width 1600px (preserving aspect ratio).
- Re-saves JPEG/PNG as optimized JPEG (quality=75) and also writes a WebP version.
- Skips the `placeholders` directory.

Run: python scripts/optimize_images.py
"""
import os
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMG_DIR = ROOT / 'assets' / 'images'
BACKUP_DIR = IMG_DIR / 'original-backups'
SKIP_DIR = IMG_DIR / 'placeholders'
MAX_WIDTH = 1600
JPEG_QUALITY = 75

def ensure_backup(path: Path):
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    dest = BACKUP_DIR / path.name
    if not dest.exists():
        path.replace(dest)
        return dest
    # if already backed up, leave original in place by copying
    return path

def process_image(path: Path):
    try:
        with Image.open(path) as img:
            img_format = img.format
            # convert PNG with alpha to RGB with white background
            if img.mode in ("RGBA", "LA"):
                background = Image.new("RGB", img.size, (255,255,255))
                background.paste(img, mask=img.split()[-1])
                img = background
            else:
                img = img.convert("RGB")

            width, height = img.size
            if width > MAX_WIDTH:
                new_h = int((MAX_WIDTH / width) * height)
                img = img.resize((MAX_WIDTH, new_h), Image.LANCZOS)

            # Save optimized JPEG (overwrite original name)
            out_jpeg_path = path
            img.save(out_jpeg_path, format='JPEG', quality=JPEG_QUALITY, optimize=True, progressive=True)

            # Also save WebP alongside
            out_webp = path.with_suffix('.webp')
            img.save(out_webp, format='WEBP', quality=JPEG_QUALITY, method=6)
            print(f"Optimized: {path.name} -> {out_jpeg_path.name}, {out_webp.name}")
    except Exception as e:
        print(f"Skipped {path}: {e}")

def main():
    if not IMG_DIR.exists():
        print(f"Images directory not found: {IMG_DIR}")
        return

    for item in IMG_DIR.iterdir():
        if item == SKIP_DIR:
            continue
        if item.is_dir():
            # skip subdirs (except we might want to process nested images later)
            continue
        if item.suffix.lower() in ('.jpg', '.jpeg', '.png'):
            # backup
            backup_target = BACKUP_DIR / item.name
            if not backup_target.exists():
                BACKUP_DIR.mkdir(parents=True, exist_ok=True)
                item.rename(backup_target)
                # move backup_target back to original path for processing
                backup_target.replace(item)
            process_image(item)
        elif item.suffix.lower() in ('.svg', '.gif'):
            print(f"Skipping vector or unsupported: {item.name}")

if __name__ == '__main__':
    main()
