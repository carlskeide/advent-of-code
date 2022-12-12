# coding=utf-8
import re

from ..utils import load_input


def parse_crates(crate_map):
    crates = {int(stack_id): [] for stack_id in crate_map[-1][1::4]}
    for line in reversed(crate_map[:-1]):
        for col, item in enumerate(line[1::4]):
            if item != " ":
                crates[col + 1].append(item)

    return crates


def move_crates(crates, moves, batch=False):
    for move in moves:
        num, src, dest = map(int, re.match(r"^move (\d+) from (\d+) to (\d+)$", move).groups())

        if batch:
            crates[dest].extend(crates[src][-num:])
            del crates[src][-num:]

        else:
            for _ in range(num):
                crates[dest].append(crates[src].pop())


if __name__ == "__main__":
    crate_map, moves = load_input(year=2022, day=5, group_lines=True)

    crates = parse_crates(crate_map.splitlines())

    move_crates(crates, moves.splitlines())
    part1 = "".join(crates[i][-1] for i in range(1,10))
    print(f"Part 1: {part1}")

    crates = parse_crates(crate_map.splitlines())
    move_crates(crates, moves.splitlines(), batch=True)
    part2 = "".join(crates[i][-1] for i in range(1,10))
    print(f"Part 2: {part2}")
