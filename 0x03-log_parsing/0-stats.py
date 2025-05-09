#!/usr/bin/python3

"""Script that reads stdin line by line and computes metrics"""

import sys


def print_stats(status_codes, total_size):
    """Print accumulated statistics"""
    print("File size: {:d}".format(total_size))
    for i in sorted(status_codes.keys()):
        if status_codes[i] != 0:
            print("{}: {:d}".format(i, status_codes[i]))


status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

line_count = 0
total_size = 0

try:
    for line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            print_stats(status_codes, total_size)

        stlist = line.split()
        line_count += 1

        try:
            total_size += int(stlist[-1])
        except Exception:
            pass

        try:
            if stlist[-2] in status_codes:
                status_codes[stlist[-2]] += 1
        except Exception:
            pass
    print_stats(status_codes, total_size)


except KeyboardInterrupt:
    print_stats(status_codes, total_size)
    raise
