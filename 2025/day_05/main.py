# https://adventofcode.com/2025/day/X
import sys


def parse_input(path: str):
    with open(path) as f:
        parts = f.read().strip().split("\n\n")
    ranges = [tuple(map(int, line.split('-'))) for line in parts[0].splitlines()]
    ids = [int(x) for x in parts[1].splitlines()]
    return ranges, ids


def merge_ranges(ranges):
    ranges.sort()
    merged = [ranges[0]]
    for low, high in ranges [1:]:
        prev_low, prev_high = merged[-1]
        if low <= prev_high + 1:
            merged[-1] = prev_low, max(prev_high, high)
        else:
            merged.append((low, high)r)
    return merged


def count_fresh(ranges, ids):
    cnt = 0
    for i in ids:
        for low, high in ranges:
            if low <= i <= high:
                cnt += 1
                break
    return cnt


def part1(ranges, ids):
    return count_fresh(ranges, ids)


def part2(ranges):
    merged = merge_ranges(ranges)
    total = sum(hi - lo + 1 for lo, hi in merged)
    return total


def main(path: str):
    ranges, ids = parse_input(path)
    print(f"Part 1: {part1(ranges, ids)}")
    print(f"Part 2: {part2(ranges)}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")

