# coding=utf-8
from . import load_input
import re


def parse_steps(instructions):
    return re.findall(r"(se|sw|nw|ne|w|e)", instructions)


def traverse(floor, steps):
    directions = {
        "nw": (-1, 1), "ne": (0, 1),
        "w": (-1, 0), "e": (1, 0),
        "sw": (0, -1), "se": (1, -1)
    }

    x, y = 0, 0
    for dx, dy in (directions[step] for step in steps):
        x, y = x + dx, y + dy

    floor[(x, y)] = (not floor.get((x, y), 0))


if __name__ == "__main__":
    task_input = load_input(day=24, group_lines=False)
    charter = [parse_steps(line) for line in task_input]
    floor = {}
    for steps in charter:
        traverse(floor, steps)

    print(f"Part 1: {sum(floor.values())}")

    part2 = ""
    print(f"Part 2: {part2}")
