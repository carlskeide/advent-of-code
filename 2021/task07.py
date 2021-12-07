# coding=utf-8
from statistics import median
from . import load_input


def fuel_consumption(crabs, target):
    return sum(abs(crab - target) for crab in crabs)


def least_fuel(crabs):
    return fuel_consumption(crabs, median(crabs))


if __name__ == "__main__":
    task_input = load_input(day=7, group_lines=False)
    crabs = [int(s) for s in task_input[0].split(',')]

    part1 = least_fuel(crabs)
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
