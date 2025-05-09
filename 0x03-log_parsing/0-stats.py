#!/usr/bin/env python3
"""
Python script that reads lines from standard input,
processes them based on the specified format, and prints the required
statistics every 10 lines or when interrupted by CTRL + C
"""


import sys
import re
from collections import defaultdict


log_pattern = re.compile(
    r'^\d{1,3}(?:\.\d{1,3}){3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
    r'"GET /projects/260 HTTP/1\.1" \d{3} \d+$'
)

total_size = 0
status_codes = defaultdict(int)
line_count = 0


def print_stats():
    """Prints the statistics of the processed lines."""
    print(f"Total size: {total_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")


try:
    for line in sys.stdin:
        line = line.strip()
        # Check if the line matches the log pattern
        if log_pattern.match(line):
            line_count += 1
            total_size += int(line.split()[-1])
            status_code = line.split()[8]
            status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_stats()
                line_count = 0
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

if line_count > 0:
    print_stats()
