#!/usr/bin/env python3
#
# find the two entries that sum to 2020 and then multiply those two numbers together.
# https://adventofcode.com/2020/day/1/input

from itertools import combinations
from math import prod


def task1(expenses, num_items):
    for items in combinations(expenses, num_items):
        if sum(items) == 2020:
            print(f"{items} = 2020")
            return prod(items)

    else:
        raise ValueError("No Match!")


if __name__ == "__main__":
    with open("./task1.input") as f:
        expenses = {int(r) for r in f.readlines()}

    print("Part 1: {}".format(task1(expenses, 2)))
    print("Part 2: {}".format(task1(expenses, 3)))
