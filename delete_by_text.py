from __future__ import annotations

import argparse
import os
import sys
from typing import List


def list_files(path: str) -> List[str]:
    try:
        entries = os.listdir(path)
    except OSError as e:
        print(f"Error reading directory {path}: {e}")
        return []
    return [f for f in entries if os.path.isfile(os.path.join(path, f))]


def find_matches(path: str, keyword: str) -> List[str]:
    files = list_files(path)
    kw = keyword.lower()
    matches = [f for f in files if kw in f.lower()]
    return matches


def delete_files(path: str, files: List[str], dry_run: bool = False) -> int:
    removed = 0
    for fname in files:
        src = os.path.join(path, fname)
        if dry_run:
            print(f"[dry-run] Would delete: {fname}")
            removed += 1
            continue
        try:
            os.remove(src)
            print(f"Deleted: {fname}")
            removed += 1
        except Exception as e:
            print(f"Failed to delete {fname}: {e}")
    return removed


def main() -> None:
    parser = argparse.ArgumentParser(description="Delete files whose names contain a keyword")
    parser.add_argument("path", nargs="?", help="Target folder path (positional)")
    parser.add_argument("value", nargs="?", help="Keyword to match (positional)")
    parser.add_argument("--path", dest="path_flag", help="Target folder path (flag)")
    parser.add_argument("--keyword", dest="keyword_flag", help="Keyword to match (flag)")
    parser.add_argument("--dry-run", action="store_true", help="Show matches without deleting")
    parser.add_argument("--yes", action="store_true", help="Proceed without confirmation")
    args = parser.parse_args()

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
        # preserve spaces in keyword
        keyword = input("Keyword to match (substring): ")
        if not keyword:
            print("No keyword provided. Exiting.")
            sys.exit(1)

    matches = find_matches(folder, keyword)
    if not matches:
        print("No matching files found.")
        return

    print(f"Found {len(matches)} matching files containing '{keyword}':")
    for m in matches:
        print(f"  {m}")

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
