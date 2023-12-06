# coding=utf-8
from ..utils import load_input
from itertools import batched
from typing import Iterable


def parse_almanac(charter: Iterable[str]) -> tuple[list, dict]:
    seeds = [int(s) for s in charter[0].split(":")[-1].split()]
    maps = {}
    for line in filter(None, charter[1:]):
        if "-to-" in line:
            cur = []
            maps[tuple(line.split()[0].split("-to-"))] = cur

        else:
            dest, src, size = map(int, line.split())
            cur.append((range(src, src + size), dest - src))

    return seeds, {types: sorted(ranges, key=lambda x: x[0].start)
                   for types, ranges in maps.items()}


def find_location(pos: int, maps: [dict]) -> int:
    src = "seed"
    dest = "?"
    while src != "location":
        dest = next(v for k, v in maps.keys() if k == src)
        for src_range, offset in maps[(src, dest)]:
            if pos in src_range:
                pos += offset
                break

        src = dest

    return pos


if __name__ == "__main__":
    task_input = load_input(year=2023, day=5, group_lines=False)
    seeds, maps = parse_almanac(task_input)

    mapped = {seed: find_location(seed, maps) for seed in seeds}
    part1 = min(mapped.values())
    print(f"Part 1: {part1}")

    seed_ranges = [
        range(start, start + size) for start, size in batched(seeds, 2)
    ]

    part2 = min(find_location(seed, maps=maps)
                for seed_range in seed_ranges
                for seed in seed_range)
    print(f"Part 2: {part2}")
