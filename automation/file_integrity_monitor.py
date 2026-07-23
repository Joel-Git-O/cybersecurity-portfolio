#!/usr/bin/env python3
"""
File Integrity Monitor - Detects unauthorized changes to files
Author: Joel Massicot
Usage: python3 file_integrity_monitor.py <directory> [--interval seconds]
"""

import hashlib
import json
import os
import sys
import time
import argparse
from datetime import datetime
from pathlib import Path


def calculate_hash(filepath: str, algorithm: str = 'sha256') -> str:
    """Calculate the hash of a file."""
    h = hashlib.new(algorithm)
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                h.update(chunk)
        return h.hexdigest()
    except (IOError, OSError) as e:
        return f"ERROR: {e}"


def build_baseline(directory: str) -> dict:
    """Scan directory and build a baseline of file hashes."""
    baseline = {}
    path = Path(directory)
    for filepath in path.rglob('*'):
        if filepath.is_file():
            rel_path = str(filepath.relative_to(path))
            baseline[rel_path] = {
                'hash': calculate_hash(str(filepath)),
                'size': filepath.stat().st_size,
                'modified': filepath.stat().st_mtime
            }
    return baseline


def check_integrity(directory: str, baseline: dict) -> dict:
    """Compare current state against baseline. Returns changes."""
    changes = {'added': [], 'removed': [], 'modified': []}
    path = Path(directory)
    current = {}

    for filepath in path.rglob('*'):
        if filepath.is_file():
            rel_path = str(filepath.relative_to(path))
            current[rel_path] = calculate_hash(str(filepath))

    for rel_path, info in baseline.items():
        if rel_path not in current:
            changes['removed'].append(rel_path)
        elif current[rel_path] != info['hash']:
            changes['modified'].append(rel_path)

    for rel_path in current:
        if rel_path not in baseline:
            changes['added'].append(rel_path)

    return changes


def save_baseline(baseline: dict, output_file: str):
    with open(output_file, 'w') as f:
        json.dump({'created': datetime.now().isoformat(), 'files': baseline}, f, indent=2)


def load_baseline(baseline_file: str) -> dict:
    with open(baseline_file, 'r') as f:
        data = json.load(f)
    return data['files']


def main():
    parser = argparse.ArgumentParser(description='File Integrity Monitor')
    parser.add_argument('directory', help='Directory to monitor')
    parser.add_argument('--baseline', default='baseline.json', help='Baseline file path')
    parser.add_argument('--interval', type=int, default=30, help='Check interval in seconds')
    parser.add_argument('--create-baseline', action='store_true', help='Create a new baseline')
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory")
        sys.exit(1)

    if args.create_baseline:
        print(f"Building baseline for: {args.directory}")
        baseline = build_baseline(args.directory)
        save_baseline(baseline, args.baseline)
        print(f"Baseline created: {len(baseline)} files tracked")
        return

    if not os.path.exists(args.baseline):
        print("No baseline found. Run with --create-baseline first.")
        sys.exit(1)

    baseline = load_baseline(args.baseline)
    print(f"File Integrity Monitor - Joel Massicot")
    print(f"Monitoring: {args.directory} | Interval: {args.interval}s")
    print("-" * 60)

    while True:
        changes = check_integrity(args.directory, baseline)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        total = sum(len(v) for v in changes.values())

        if total > 0:
            print(f"[{timestamp}] ALERT: {total} change(s) detected")
            for f in changes['added']:
                print(f"  [+] ADDED:    {f}")
            for f in changes['modified']:
                print(f"  [!] MODIFIED: {f}")
            for f in changes['removed']:
                print(f"  [-] REMOVED:  {f}")
        else:
            print(f"[{timestamp}] OK - No changes ({len(baseline)} files monitored)")

        time.sleep(args.interval)


if __name__ == "__main__":
    main()
