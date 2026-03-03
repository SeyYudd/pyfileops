from __future__ import annotations

import os
import shutil
import sys
from typing import Dict, List


# Bagian ini yang harus di ganti: sesuaikan peta ekstensi -> nama folder.
# Contoh: jika Anda ingin .pdf ke folder 'PDFs' ubah ".pdf": "Documents" -> ".pdf": "PDFs"
EXTENSION_MAP: Dict[str, str] = {
    # images
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    # documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".md": "Documents",
    # spreadsheets
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    # archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
}


def list_files(path: str) -> List[str]:
    try:
        entries = os.listdir(path)
    except OSError as e:
        print(f"Error reading directory {path}: {e}")
        return []
    return [f for f in entries if os.path.isfile(os.path.join(path, f))]


def target_folder_for_extension(ext: str) -> str:
    # Bagian ini yang harus di ganti: default fallback 'Others' bisa diubah
    # ke nama folder lain jika diinginkan.
    return EXTENSION_MAP.get(ext.lower(), "Others")


def unique_destination(dest_dir: str, desired_name: str) -> str:
    base, ext = os.path.splitext(desired_name)
    candidate = os.path.join(dest_dir, desired_name)
    counter = 1
    while os.path.exists(candidate):
        candidate_name = f"{base}_{counter}{ext}"
        candidate = os.path.join(dest_dir, candidate_name)
        counter += 1
    return candidate


def group_by_type(path: str) -> int:
    files = list_files(path)
    processed = 0
    for fname in files:
        src = os.path.join(path, fname)
        _, ext = os.path.splitext(fname)
        folder = target_folder_for_extension(ext)
        dest_dir = os.path.join(path, folder)
        os.makedirs(dest_dir, exist_ok=True)
        final = unique_destination(dest_dir, fname)
        try:
            shutil.move(src, final)
            print(f"Moved {fname} -> {folder}/{os.path.basename(final)}")
            processed += 1
        except Exception as e:
            print(f"Failed to move {fname}: {e}")
    return processed


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Organize files into folders by extension")
    parser.add_argument("path", nargs="?", help="Target folder path (positional)")
    parser.add_argument("--path", dest="path_flag", help="Target folder path (flag)")
    args = parser.parse_args()

    print("group_by_type — organize files into folders by extension")
    folder = args.path or args.path_flag
    if not folder:
        folder = input("Folder path: ").strip()
    if not folder:
        print("No folder provided. Exiting.")
        sys.exit(1)
    if not os.path.isdir(folder):
        print("Folder does not exist or is not a directory.")
        sys.exit(1)
    total = group_by_type(folder)
    print(f"\nSummary: {total} files moved.")


if __name__ == "__main__":
    main()
