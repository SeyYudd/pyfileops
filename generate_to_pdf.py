#!/usr/bin/env python3
from __future__ import annotations
import argparse
import os
import sys
from typing import List
from PIL import Image, ImageDraw, ImageFont

def list_files(path: str) -> List[str]:
    try:
        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    except Exception:
        return []

def unique_destination(dest_dir: str, desired_name: str) -> str:
    base, ext = os.path.splitext(desired_name)
    candidate = os.path.join(dest_dir, desired_name)
    counter = 1
    while os.path.exists(candidate):
        candidate_name = f"{base}_{counter}{ext}"
        candidate = os.path.join(dest_dir, candidate_name)
        counter += 1
    return candidate

def image_to_pdf(src_path: str, dest_path: str) -> None:
    im = Image.open(src_path)
    if im.mode in ("RGBA", "LA"):
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    im.save(dest_path, "PDF", resolution=100.0)

def text_to_pdf(src_path: str, dest_path: str) -> None:
    with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.read().splitlines()
    font = ImageFont.load_default()
    max_width = 1200
    line_height = font.getsize("A")[1] + 4
    img_height = max(800, line_height * (len(lines) + 2))
    img = Image.new("RGB", (max_width, img_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    y = 10
    margin = 10
    for line in lines:
        draw.text((margin, y), line, font=font, fill=(0, 0, 0))
        y += line_height
    img = img.crop((0, 0, max_width, y + margin))
    img.save(dest_path, "PDF", resolution=100.0)

def convert_file(src: str, dry_run: bool = False) -> bool:
    supported_images = {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp"}
    base, ext = os.path.splitext(src)
    ext = ext.lower()
    dest = base + ".pdf"
    dest = unique_destination(os.path.dirname(src), os.path.basename(dest))
    if dry_run:
        print(f"[dry-run] Would convert: {src} -> {dest}")
        return True
    try:
        if ext in supported_images:
            image_to_pdf(src, dest)
            print(f"Converted image: {src} -> {dest}")
            return True
        elif ext == ".txt":
            text_to_pdf(src, dest)
            print(f"Converted text: {src} -> {dest}")
            return True
        elif ext == ".pdf":
            print(f"Skipping PDF: {src}")
            return False
        else:
            try:
                image_to_pdf(src, dest)
                print(f"Converted unknown as image: {src} -> {dest}")
                return True
            except Exception:
                print(f"Unsupported file type, skipped: {src}")
                return False
    except Exception as e:
        print(f"Failed to convert {src}: {e}")
        return False

def main() -> None:
    parser = argparse.ArgumentParser(description="Convert images/text to PDF")
    parser.add_argument("path", nargs="?", help="File or folder path (positional)")
    parser.add_argument("--path", dest="path_flag", help="File or folder path (flag)")
    parser.add_argument("--batch", action="store_true", help="If path is folder, convert all supported files")
    parser.add_argument("--dry-run", action="store_true", help="Preview conversions")
    args = parser.parse_args()

    p = args.path or args.path_flag
    if not p:
        p = input("File or folder path: ").strip()
    if not p:
        print("No path provided. Exiting.")
        sys.exit(1)
    if os.path.isfile(p):
        convert_file(p, dry_run=args.dry_run)
        return
    if os.path.isdir(p):
        if not args.batch:
            print("Path is a folder. Use --batch to convert all files inside.")
            return
        files = list_files(p)
        converted = 0
        for f in files:
            full = os.path.join(p, f)
            if convert_file(full, dry_run=args.dry_run):
                converted += 1
        print(f"\nSummary: {converted} files converted.")

if __name__ == "__main__":
    main()
