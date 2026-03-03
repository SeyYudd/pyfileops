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


def suffix_files(path: str, suffix: str) -> int:
    files = list_files(path)
    processed = 0
    for fname in files:
        base, ext = os.path.splitext(fname)
        # Bagian ini yang harus di ganti: aturan deteksi double-suffix.
        # Saat ini menggunakan pemeriksaan case-insensitive endswith.
        if base.lower().endswith(suffix.lower()):
            print(f"Skipping (already suffixed): {fname}")
            continue
        new_name = f"{base}{suffix}{ext}"
        src = os.path.join(path, fname)
        dst = os.path.join(path, new_name)
        # collision handling
        # Bagian ini yang harus di ganti: format penanganan collision.
        # Saat ini menambahkan _1, _2, dll. Ubah jika Anda ingin format lain.
        counter = 1
        final_dst = dst
        b2, e2 = os.path.splitext(new_name)
        while os.path.exists(final_dst):
            cand = f"{b2}_{counter}{e2}"
            final_dst = os.path.join(path, cand)
            counter += 1
        try:
            os.rename(src, final_dst)
            print(f"Renamed: {fname} -> {os.path.basename(final_dst)}")
            processed += 1
        except Exception as e:
            print(f"Failed to rename {fname}: {e}")
    return processed


def main() -> None:
    parser = argparse.ArgumentParser(description="Add a suffix before file extensions")
    parser.add_argument("path", nargs="?", help="Target folder path (positional)")
    parser.add_argument("value", nargs="?", help="Suffix to add (positional)")
    parser.add_argument("--path", dest="path_flag", help="Target folder path (flag)")
    parser.add_argument("--suffix", dest="suffix_flag", help="Suffix to add (flag)")
    args = parser.parse_args()

    print("file_suffixer — add a suffix before file extensions")
    folder = args.path or args.path_flag
    suffix = args.value or args.suffix_flag

    if not folder:
        folder = input("Folder path: ").strip()
    if not folder:
        print("No folder provided. Exiting.")
        sys.exit(1)
    if not os.path.isdir(folder):
        print("Folder does not exist or is not a directory.")
        sys.exit(1)

    if suffix is None:
        # preserve spaces user types for suffix
        suffix = input("Suffix to add (default '_anggur'): ") or "_anggur"

    total = suffix_files(folder, suffix)
    print(f"\nSummary: {total} files renamed.")


if __name__ == "__main__":
    main()
