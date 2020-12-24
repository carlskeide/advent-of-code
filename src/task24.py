# coding=utf-8
from . import load_input

import re
from collections import defaultdict

DIRECTIONS = {
    "nw": (0, -1, 1), "ne": (1, -1, 0),
    "w": (-1, 0, 1), "e": (1, 0, -1),
    "sw": (-1, 1, 0), "se": (0, 1, -1)
}


def parse_steps(instructions):
    return re.findall(r"(se|sw|nw|ne|w|e)", instructions)


def traverse(floor, steps):
    x = y = z = 0
    for dx, dy, dz in (DIRECTIONS[step] for step in steps):
        x, y, z = x + dx, y + dy, z + dz

    floor[(x, y, z)] = not floor[(x, y, z)]


def neighbors(x, y, z):
    return (((x + dx, y + dy, z + dz) for dx, dy, dz in DIRECTIONS.values()))


def flip(floor):
    for coords in list(floor.keys()):
        for neighbor in neighbors(*coords):
            _ = floor[neighbor]

    new_floor = defaultdict(int)
    for coords in list(floor.keys()):
        tile = floor[coords]
        adjacent = sum(floor[neighbor] for neighbor in neighbors(*coords))
        if tile and (adjacent == 0 or adjacent > 2):
            new_floor[coords] = 0

        elif not tile and adjacent == 2:
            new_floor[coords] = 1

        else:
            new_floor[coords] = floor[coords]

    return new_floor


if __name__ == "__main__":
    task_input = load_input(day=24)
    charter = [parse_steps(line) for line in task_input]
    floor = defaultdict(int)
    for steps in charter:
        traverse(floor, steps)

    print(f"Part 1: {sum(floor.values())}")

    for _ in range(100):
        floor = flip(floor)

    print(f"Part 2: {sum(floor.values())}")
