# coding=utf-8
from . import load_input

from itertools import combinations
from math import prod


def find_expences(expenses, num_items):
    for items in combinations(expenses, num_items):
        if sum(items) == 2020:
            print(f"{items} = 2020")
            return prod(items)

    else:
        raise ValueError("No Match!")


if __name__ == "__main__":
    expenses = {int(r) for r in load_input(day=1)}

    print("Part 1: {}".format(find_expences(expenses, 2)))
    print("Part 2: {}".format(find_expences(expenses, 3)))
