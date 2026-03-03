from __future__ import annotations

import argparse
import os
import sys


def list_files(path: str) -> list[str]:
    try:
        entries = os.listdir(path)
    except OSError as e:
        print(f"Error reading directory {path}: {e}")
        return []
    return [f for f in entries if os.path.isfile(os.path.join(path, f))]


def prefix_files(path: str, prefix: str) -> int:
    files = list_files(path)
    processed = 0
    for fname in files:
        # skip directories and already-prefixed files (case-insensitive)
        if fname.lower().startswith(prefix.lower()):
            print(f"Skipping (already prefixed): {fname}")
            continue
        src = os.path.join(path, fname)
        new_name = prefix + fname
        dst = os.path.join(path, new_name)
        # collision handling: append _1, _2, ... before extension
        base, ext = os.path.splitext(new_name)
        counter = 1
        final_dst = dst
        while os.path.exists(final_dst):
            final_name = f"{base}_{counter}{ext}"
            final_dst = os.path.join(path, final_name)
            counter += 1
        try:
            os.rename(src, final_dst)
            print(f"Renamed: {fname} -> {os.path.basename(final_dst)}")
            processed += 1
        except Exception as e:
            print(f"Failed to rename {fname}: {e}")
    return processed


def main() -> None:
    parser = argparse.ArgumentParser(description="Add a prefix to files in a folder")
    parser.add_argument("path", nargs="?", help="Target folder path (positional)")
    parser.add_argument("value", nargs="?", help="Prefix to add (positional)")
    parser.add_argument("--path", dest="path_flag", help="Target folder path (flag)")
    parser.add_argument("--prefix", dest="prefix_flag", help="Prefix to add (flag)")
    args = parser.parse_args()

    # Determine folder and prefix: positional > flag > interactive
    folder = args.path or args.path_flag
    prefix = args.value or args.prefix_flag

    if not folder:
        folder = input("Folder path: ").strip()
    if not folder:
        print("No folder provided. Exiting.")
        sys.exit(1)
    if not os.path.isdir(folder):
        print("Folder does not exist or is not a directory.")
        sys.exit(1)

    if prefix is None:
        # preserve leading/trailing spaces the user types (do not strip)
        prefix = input("Prefix to add (default 'anggur_'): ") or "anggur_"

    total = prefix_files(folder, prefix)
    print(f"\nSummary: {total} files renamed.")


if __name__ == "__main__":
    main()
