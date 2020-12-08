# coding=utf-8
from utils import load_input

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
    expenses = {int(r) for r in load_input(day=1)}

    print("Part 1: {}".format(task1(expenses, 2)))
    print("Part 2: {}".format(task1(expenses, 3)))
