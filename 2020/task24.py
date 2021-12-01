# coding=utf-8
from . import load_input

import re
from collections import defaultdict

DIRECTIONS = {
    "nw": (-1, 1), "ne": (0, 1),
    "w": (-1, 0), "e": (1, 0),
    "sw": (0, -1), "se": (1, -1)
}


def parse_steps(instructions):
    return re.findall(r"(se|sw|nw|ne|w|e)", instructions)


def traverse(floor, steps):
    x = y = 0
    for dx, dy in (DIRECTIONS[step] for step in steps):
        x, y = x + dx, y + dy

    floor[(x, y)] = not floor[(x, y)]


def neighbors(x, y):
    return (((x + dx, y + dy) for dx, dy in DIRECTIONS.values()))


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
