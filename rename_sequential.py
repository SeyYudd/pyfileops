#!/usr/bin/env python3
from __future__ import annotations
import argparse
import os
import sys
import uuid
from typing import List, Tuple

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

def build_targets(files: List[str], prefix: str, start: int, digits: int,
                  new_ext: str|None, path: str) -> List[Tuple[str,str]]:
    targets: List[Tuple[str,str]] = []
    n = start
    for fn in files:
        base, ext = os.path.splitext(fn)
        ext_to_use = ('.' + new_ext.lstrip('.')) if new_ext else ext
        target_name = f"{prefix}{str(n).zfill(digits)}{ext_to_use}"
        target_full = os.path.join(path, target_name)
        if os.path.exists(target_full) and target_full not in [os.path.join(path, f) for f in files]:
            target_full = unique_destination(path, target_name)
        targets.append((fn, os.path.basename(target_full)))
        n += 1
    return targets

def perform_renames(path: str, mapping: List[Tuple[str,str]], dry_run: bool=False) -> int:
    temp_map: List[Tuple[str,str]] = []
    for src, tgt in mapping:
        src_full = os.path.join(path, src)
        tmp_name = f".tmp_rename_{uuid.uuid4().hex}"
        tmp_full = os.path.join(path, tmp_name)
        temp_map.append((src_full, tmp_full))
    if dry_run:
        print("[dry-run] Rename plan:")
        for (s,t) in mapping:
            print(f"  {s} -> {t}")
        return 0
    for (src_full, tmp_full) in temp_map:
        os.rename(src_full, tmp_full)
    renamed = 0
    for ((_, tgt), (_, tmp_full)) in zip(mapping, temp_map):
        final_full = os.path.join(path, tgt)
        if os.path.exists(final_full):
            final_full = unique_destination(path, tgt)
        os.rename(tmp_full, final_full)
        renamed += 1
    return renamed

def main() -> None:
    parser = argparse.ArgumentParser(description='Sequential rename files in a folder')
    parser.add_argument('path', nargs='?', help='Folder path')
    parser.add_argument('--path', dest='path_flag', help='Folder path (flag)')
    parser.add_argument('--prefix', default='', help='Prefix for filenames')
    parser.add_argument('--start', type=int, default=1, help='Start number (default 1)')
    parser.add_argument('--digits', type=int, default=3, help='Zero-padding digits (default 3)')
    parser.add_argument('--ext', help='Filter by extension (e.g. jpg or .jpg)')
    parser.add_argument('--new-ext', help='Change extension for targets (e.g. pdf)')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes')
    parser.add_argument('--yes', action='store_true', help='Assume yes for confirmations')
    args = parser.parse_args()

    p = args.path or args.path_flag
    if not p:
        p = input('Folder path: ').strip()
    if not p:
        print('No path provided. Exiting.')
        sys.exit(1)
    if not os.path.isdir(p):
        print('Path is not a directory. Exiting.')
        sys.exit(1)

    files = sorted(list_files(p))
    if args.ext:
        ext = args.ext if args.ext.startswith('.') else '.' + args.ext
        files = [f for f in files if f.lower().endswith(ext.lower())]

    if not files:
        print('No matching files found.')
        return

    mapping = build_targets(files, args.prefix, args.start, args.digits, args.new_ext, p)

    if args.dry_run:
        print('[dry-run] Planned renames:')
        for src, tgt in mapping:
            print(f'  {src} -> {tgt}')
        return

    if not args.yes:
        print('Planned renames:')
        for src, tgt in mapping:
            print(f'  {src} -> {tgt}')
        resp = input('Proceed? [y/N]: ').strip().lower()
        if resp not in ('y','yes'):
            print('Aborted.')
            return

    renamed = perform_renames(p, mapping, dry_run=False)
    print(f'Renamed {renamed} files.')

if __name__ == '__main__':
    main()
