#!/usr/bin/env python3
from __future__ import annotations
import argparse
import os
import sys

def find_empty_dirs(path: str):
    empty = []
    for root, dirs, files in os.walk(path, topdown=False):
        if not dirs and not files:
            empty.append(root)
    return empty

def remove_dirs(dirs, dry_run=False):
    removed = 0
    for d in dirs:
        if dry_run:
            print(f"[dry-run] Would remove: {d}")
            removed += 1
            continue
        try:
            os.rmdir(d)
            print(f"Removed: {d}")
            removed += 1
        except Exception as e:
            print(f"Failed to remove {d}: {e}")
    return removed

def main():
    parser = argparse.ArgumentParser(description="Remove empty folders under a path")
    parser.add_argument("path", nargs="?", help="Target folder path (positional)")
    parser.add_argument("--path", dest="path_flag", help="Target folder path (flag)")
    parser.add_argument("--dry-run", action="store_true", help="Show matches without deleting")
    parser.add_argument("--yes", action="store_true", help="Proceed without confirmation")
    args = parser.parse_args()

    folder = args.path or args.path_flag
    if not folder:
        folder = input("Folder path: ").strip()
    if not folder:
        print("No folder provided. Exiting.")
        sys.exit(1)
    if not os.path.isdir(folder):
        print("Folder does not exist or is not a directory.")
        sys.exit(1)

    empties = find_empty_dirs(folder)
    if not empties:
        print("No empty folders found.")
        return

    print(f"Found {len(empties)} empty folders:")
    for d in empties:
        print(f"  {d}")

    if args.dry_run:
        print("\nDry-run mode, no folders were removed.")
        return

    if not args.yes:
        confirm = input(f"\nProceed to remove these {len(empties)} folders? (y/N): ").strip().lower()
        if confirm != "y":
            print("Aborted by user.")
            return

    removed = remove_dirs(empties, dry_run=False)
    print(f"\nSummary: {removed} folders removed.")

if __name__ == "__main__":
    main()
