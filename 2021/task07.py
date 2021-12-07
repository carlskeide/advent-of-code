# coding=utf-8
from statistics import median
from . import load_input


def linear_fuel(crabs, target):
    return sum(abs(crab - target) for crab in crabs)


def exponential_fuel(crabs, target):
    return sum(sum(range(abs(crab - target) + 1)) for crab in crabs)


if __name__ == "__main__":
    task_input = load_input(day=7, group_lines=False)
    crabs = [int(s) for s in task_input[0].split(',')]

    part1 = linear_fuel(crabs, median(crabs))
    print(f"Part 1: {part1}")

    part2 = min(
        exponential_fuel(crabs, pos)
        for pos in range(min(crabs), max(crabs) + 1)
    )
    print(f"Part 2: {part2}")
