from __future__ import annotations

import argparse
import os
import re
import sys
from typing import List, Tuple


def list_files(path: str) -> List[str]:
    try:
        entries = os.listdir(path)
    except OSError as e:
        print(f"Error reading directory {path}: {e}")
        return []
    return [f for f in entries if os.path.isfile(os.path.join(path, f))]


def build_new_name(fname: str, old: str, new: str) -> str:
    # replace all occurrences case-insensitively
    pattern = re.compile(re.escape(old), flags=re.IGNORECASE)
    return pattern.sub(new, fname)


def find_renames(path: str, old: str, new: str) -> List[Tuple[str, str]]:
    files = list_files(path)
    renames: List[Tuple[str, str]] = []
    for f in files:
        if re.search(re.escape(old), f, flags=re.IGNORECASE):
            new_name = build_new_name(f, old, new)
            if new_name != f:
                renames.append((f, new_name))
    return renames


def unique_destination(dest_dir: str, desired_name: str) -> str:
    base, ext = os.path.splitext(desired_name)
    candidate = os.path.join(dest_dir, desired_name)
    counter = 1
    while os.path.exists(candidate):
        candidate_name = f"{base}_{counter}{ext}"
        candidate = os.path.join(dest_dir, candidate_name)
        counter += 1
    return candidate


def perform_renames(path: str, renames: List[Tuple[str, str]], dry_run: bool = False) -> int:
    performed = 0
    for src_name, desired in renames:
        src = os.path.join(path, src_name)
        if dry_run:
            print(f"[dry-run] {src_name} -> {desired}")
            performed += 1
            continue
        final = unique_destination(path, desired)
        try:
            os.rename(src, final)
            print(f"Renamed: {src_name} -> {os.path.basename(final)}")
            performed += 1
        except Exception as e:
            print(f"Failed to rename {src_name}: {e}")
    return performed


def main() -> None:
    parser = argparse.ArgumentParser(description="Rename files by replacing text in filenames")
    parser.add_argument("path", nargs="?", help="Target folder path (positional)")
    parser.add_argument("old", nargs="?", help="Old substring to replace (positional)")
    parser.add_argument("new", nargs="?", help="New substring (positional)")
    parser.add_argument("--path", dest="path_flag", help="Target folder path (flag)")
    parser.add_argument("--old", dest="old_flag", help="Old substring (flag)")
    parser.add_argument("--new", dest="new_flag", help="New substring (flag)")
    parser.add_argument("--dry-run", action="store_true", help="Show renames without performing them")
    parser.add_argument("--yes", action="store_true", help="Proceed without confirmation")
    args = parser.parse_args()

    folder = args.path or args.path_flag
    old = args.old or args.old_flag
    new = args.new or args.new_flag

    if not folder:
        folder = input("Folder path: ").strip()
    if not folder:
        print("No folder provided. Exiting.")
        sys.exit(1)
    if not os.path.isdir(folder):
        print("Folder does not exist or is not a directory.")
        sys.exit(1)

    if old is None:
        old = input("Old substring to replace: ")
        if not old:
            print("No old substring provided. Exiting.")
            sys.exit(1)
    if new is None:
        # preserve spaces in replacement
        new = input("New substring: ")

    renames = find_renames(folder, old, new)
    if not renames:
        print("No filenames matched the given substring.")
        return

    print(f"Found {len(renames)} files to rename:")
    for s, d in renames:
        print(f"  {s} -> {d}")

    if args.dry_run:
        print("\nDry-run mode, no files were changed.")
        return

    if not args.yes:
        confirm = input(f"\nGANTI SEMUA NAMA FILE {len(renames)} files? (y/N): ").strip().lower()
        if confirm != "y":
            print("Aborted by user.")
            return

    performed = perform_renames(folder, renames, dry_run=False)
    print(f"\nSummary: {performed} files renamed.")


if __name__ == "__main__":
    main()
