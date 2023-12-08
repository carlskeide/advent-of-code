# coding=utf-8
from ..utils import load_input
from itertools import cycle
from math import lcm
import re


def traverse(
    directions: str,
    nodes: dict[str, tuple[str, str]],
    start: str = "AAA",
    target: str = "ZZZ"
) -> int:
    cur = start
    for i, direction in enumerate(cycle(directions)):
        if re.match(target, cur):
            return i
        else:
            cur = nodes[cur]["LR".index(direction)]


def least_steps(directions: str, nodes: dict[str, tuple[str, str]]) -> int:
    paths = [
        traverse(directions, nodes, node, r"..Z")
        for node in nodes if re.match(r"..A", node)
    ]
    return lcm(*paths)


if __name__ == "__main__":
    task_input = load_input(year=2023, day=8, group_lines=False)
    directions = task_input[0]
    nodes = {
        node: (l, r) for node, l, r in (
            re.match(r"(\w+) = \((\w+), (\w+)\)", line).groups()
            for line in task_input[2:]
        )
    }

    part1 = traverse(directions, nodes)
    print(f"Part 1: {part1}")

    part2 = least_steps(directions, nodes)
    print(f"Part 2: {part2}")
