"""Summarize failed SSH sign-ins from a local text log. Python 3.9+."""
import argparse
from collections import Counter
import re
from pathlib import Path

FAILED_SSH = re.compile(r"Failed password for (?:invalid user )?\S+ from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})")

def analyze(text: str) -> Counter:
    """Count matching failed SSH logins by source IPv4 address."""
    counts = Counter()
    for line in text.splitlines():
        match = FAILED_SSH.search(line)
        if match:
            counts[match.group('ip')] += 1
    return counts

def main() -> None:
    parser = argparse.ArgumentParser(description='Summarize failed SSH attempts in a local log file.')
    parser.add_argument('logfile', type=Path)
    parser.add_argument('--threshold', type=int, default=3, help='Minimum failures to flag (default: 3)')
    args = parser.parse_args()
    if args.threshold < 1:
        parser.error('--threshold must be >= 1')
    try:
        counts = analyze(args.logfile.read_text(encoding='utf-8', errors='replace'))
    except OSError as exc:
        parser.error(str(exc))
    if not counts:
        print('No matching failed SSH login entries found.')
        return
    print('Failed SSH logins by source IP:')
    for ip, count in counts.most_common():
        label = ' [REVIEW]' if count >= args.threshold else ''
        print(f'{ip}: {count}{label}')
    print('\nNote: REVIEW means threshold reached, not proof of an attack.')

if __name__ == '__main__':
    main()
