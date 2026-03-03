from __future__ import annotations

import argparse
import os
import shutil
import sys


def list_files(path: str) -> list[str]:
    try:
        entries = os.listdir(path)
    except OSError as e:
        print(f"Error reading directory {path}: {e}")
        return []
    return [f for f in entries if os.path.isfile(os.path.join(path, f))]


def unique_destination(dest_dir: str, desired_name: str) -> str:
    base, ext = os.path.splitext(desired_name)
    candidate = os.path.join(dest_dir, desired_name)
    counter = 1
    while os.path.exists(candidate):
        candidate_name = f"{base}_{counter}{ext}"
        candidate = os.path.join(dest_dir, candidate_name)
        counter += 1
    return candidate


def group_by_text(path: str, keyword: str) -> int:
    files = list_files(path)
    processed = 0
    dest_dir = os.path.join(path, keyword)
    for fname in files:
        # Bagian ini yang harus di ganti: metode pencocokan kata.
        # Saat ini menggunakan pemeriksaan substring case-insensitive.
        if keyword.lower() in fname.lower():
            src = os.path.join(path, fname)
            os.makedirs(dest_dir, exist_ok=True)
            final = unique_destination(dest_dir, fname)
            try:
                shutil.move(src, final)
                print(f"Moved {fname} -> {keyword}/{os.path.basename(final)}")
                processed += 1
            except Exception as e:
                print(f"Failed to move {fname}: {e}")
    return processed


def main() -> None:
    parser = argparse.ArgumentParser(description="Move files containing a keyword into a named folder")
    parser.add_argument("path", nargs="?", help="Target folder path (positional)")
    parser.add_argument("value", nargs="?", help="Keyword to match (positional)")
    parser.add_argument("--path", dest="path_flag", help="Target folder path (flag)")
    parser.add_argument("--keyword", dest="keyword_flag", help="Keyword to match (flag)")
    args = parser.parse_args()

    print("group_by_text — move files containing a keyword into a named folder")
    folder = args.path or args.path_flag
    keyword = args.value or args.keyword_flag

    if not folder:
        folder = input("Folder path: ").strip()
    if not folder:
        print("No folder provided. Exiting.")
        sys.exit(1)
    if not os.path.isdir(folder):
        print("Folder does not exist or is not a directory.")
        sys.exit(1)

    if keyword is None:
        # preserve spaces in keyword entered by user
        keyword = input("Keyword to match (default 'anggur'): ") or "anggur"

    total = group_by_text(folder, keyword)
    print(f"\nSummary: {total} files moved into folder '{keyword}'.")


if __name__ == "__main__":
    main()
