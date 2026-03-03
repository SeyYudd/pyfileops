#!/usr/bin/env python3
from __future__ import annotations
import argparse
import os
import sys

def list_files(path: str):
    try:
        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    except OSError as e:
        print(f"Error reading directory {path}: {e}")
        return []

def find_by_size(path: str, min_kb: int, max_kb: int):
    matches = []
    for f in list_files(path):
        p = os.path.join(path, f)
        try:
            size = os.path.getsize(p) // 1024
        except Exception:
            continue
        if min_kb <= size <= max_kb:
            matches.append((f, size))
    return matches

def delete_files(path: str, files, dry_run=False):
    removed = 0
    for fname, sz in files:
        p = os.path.join(path, fname)
        if dry_run:
            print(f"[dry-run] Would delete: {fname} ({sz} KB)")
            removed += 1
            continue
        try:
            os.remove(p)
            print(f"Deleted: {fname} ({sz} KB)")
            removed += 1
        except Exception as e:
            print(f"Failed to delete {fname}: {e}")
    return removed

def main():
    parser = argparse.ArgumentParser(description="Delete files by size range (KB)")
    parser.add_argument("path", nargs="?", help="Target folder path (positional)")
    parser.add_argument("min_kb", nargs="?", type=int, help="Min size in KB (positional)")
    parser.add_argument("max_kb", nargs="?", type=int, help="Max size in KB (positional)")
    parser.add_argument("--path", dest="path_flag", help="Target folder path (flag)")
    parser.add_argument("--min", dest="min_flag", type=int, help="Min size in KB (flag)")
    parser.add_argument("--max", dest="max_flag", type=int, help="Max size in KB (flag)")
    parser.add_argument("--dry-run", action="store_true", help="Show matches without deleting")
    parser.add_argument("--yes", action="store_true", help="Proceed without confirmation")
    args = parser.parse_args()

    folder = args.path or args.path_flag
    min_kb = args.min_kb or args.min_flag
    max_kb = args.max_kb or args.max_flag

    if not folder:
        folder = input("Folder path: ").strip()
    if not folder:
        print("No folder provided. Exiting.")
        sys.exit(1)
    if not os.path.isdir(folder):
        print("Folder does not exist or is not a directory.")
        sys.exit(1)

    if min_kb is None:
        try:
            min_kb = int(input("Min size in KB: ").strip())
        except Exception:
            print("Invalid min size. Exiting.")
            sys.exit(1)
    if max_kb is None:
        try:
            max_kb = int(input("Max size in KB: ").strip())
        except Exception:
            print("Invalid max size. Exiting.")
            sys.exit(1)

    matches = find_by_size(folder, min_kb, max_kb)
    if not matches:
        print("No files found in the given size range.")
        return

    print(f"Found {len(matches)} files between {min_kb} KB and {max_kb} KB:")
    for f, s in matches:
        print(f"  {f} ({s} KB)")

    if args.dry_run:
        print("\nDry-run mode, no files were deleted.")
        return

    if not args.yes:
        confirm = input(f"\nProceed to delete these {len(matches)} files? (y/N): ").strip().lower()
        if confirm != "y":
            print("Aborted by user.")
            return

    removed = delete_files(folder, matches, dry_run=False)
    print(f"\nSummary: {removed} files deleted.")

if __name__ == "__main__":
    main()
