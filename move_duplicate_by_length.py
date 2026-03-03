#!/usr/bin/env python3
from __future__ import annotations
import argparse
import os
import shutil
import sys
from collections import defaultdict
from typing import Dict, List, Tuple

DUPLICATE_FOLDER = "THIS IS DUPLICATE"


def list_files(path: str) -> List[str]:
    try:
        return [
            f for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f))
        ]
    except Exception:
        return []


def make_key(filename: str, length: int, include_ext: bool) -> str:
    if include_ext:
        return filename[:length].lower()
    base, _ = os.path.splitext(filename)
    return base[:length].lower()


def find_duplicates(
    files: List[str], length: int, include_ext: bool
) -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = defaultdict(list)
    for f in files:
        key = make_key(f, length, include_ext)
        groups[key].append(f)
    return {k: v for k, v in groups.items() if len(v) > 1}


def unique_destination(dest_dir: str, desired_name: str) -> str:
    base, ext = os.path.splitext(desired_name)
    candidate = os.path.join(dest_dir, desired_name)
    counter = 1
    while os.path.exists(candidate):
        candidate = os.path.join(dest_dir, f"{base}_{counter}{ext}")
        counter += 1
    return candidate


def move_files(
    path: str,
    duplicates: Dict[str, List[str]],
    dry_run: bool = False,
) -> int:
    dest_dir = os.path.join(path, DUPLICATE_FOLDER)
    if not dry_run and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    moved = 0
    for key, files in duplicates.items():
        print(f"\nGroup [{key!r}]:")
        for fn in files:
            src = os.path.join(path, fn)
            final = unique_destination(dest_dir, fn)
            dest_name = os.path.basename(final)
            if dry_run:
                print(f"  [dry-run] {fn} -> {DUPLICATE_FOLDER}/{dest_name}")
            else:
                shutil.move(src, final)
                print(f"  Moved: {fn} -> {DUPLICATE_FOLDER}/{dest_name}")
                moved += 1
    return moved


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Move files with matching first N chars to duplicate folder"
    )
    parser.add_argument("path", nargs="?", help="Folder path")
    parser.add_argument("--path", dest="path_flag", help="Folder path (flag)")
    parser.add_argument(
        "--length", type=int, default=50,
        help="Number of chars to compare (default: 50)"
    )
    parser.add_argument(
        "--include-ext", choices=["y", "n"], default=None,
        help="Include extension in comparison? y=yes, n=no (default: ask)"
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation")
    args = parser.parse_args()

    p = args.path or args.path_flag
    if not p:
        p = input("Folder path: ").strip()
    if not p:
        print("No path provided. Exiting.")
        sys.exit(1)
    if not os.path.isdir(p):
        print("Path is not a directory. Exiting.")
        sys.exit(1)

    # resolve include-ext
    include_ext_flag = args.include_ext
    if include_ext_flag is None:
        ans = input("Include extension in comparison? [y/N]: ").strip().lower()
        include_ext_flag = "y" if ans in ("y", "yes") else "n"
    include_ext = include_ext_flag == "y"

    mode_label = "nama + ekstensi" if include_ext else "nama saja (tanpa ekstensi)"
    print(f"\nMode perbandingan : {mode_label}")
    print(f"Panjang karakter  : {args.length}")

    files = list_files(p)
    # exclude the duplicate folder itself
    files = [f for f in files if f != DUPLICATE_FOLDER]

    duplicates = find_duplicates(files, args.length, include_ext)

    if not duplicates:
        print("\nTidak ada duplikat ditemukan.")
        return

    total = sum(len(v) for v in duplicates.values())
    print(f"\nDitemukan {total} file dalam {len(duplicates)} grup duplikat.\n")

    if args.dry_run:
        move_files(p, duplicates, dry_run=True)
        return

    if not args.yes:
        for key, files_in_group in duplicates.items():
            print(f"  [{key!r}]: {', '.join(files_in_group)}")
        resp = input("\nPindahkan semua ke folder 'THIS IS DUPLICATE'? [y/N]: ").strip().lower()
        if resp not in ("y", "yes"):
            print("Dibatalkan.")
            return

    moved = move_files(p, duplicates, dry_run=False)
    print(f"\nSelesai. {moved} file dipindahkan ke '{DUPLICATE_FOLDER}'.")


if __name__ == "__main__":
    main()
