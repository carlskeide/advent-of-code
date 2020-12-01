#!/usr/bin/env python3
#
# find the two entries that sum to 2020 and then multiply those two numbers together.
# https://adventofcode.com/2020/day/1/input


def part1(expenses):
    for item in expenses:
        needle = abs(item - 2020)
        if needle in expenses:
            print(f"{item} + {needle} = 2020")
            return item * needle

    else:
        raise ValueError("No Match!")


def part2(expenses):
    for item in expenses:
        for item2 in expenses:
            for item3 in expenses:
                if sum((item, item2, item3)) == 2020:
                    print(f"{item} * {item2} * {item3} = 2020")
                    return item * item2 * item3

    else:
        raise ValueError("No Match!")


if __name__ == "__main__":
    with open("./task1.input") as f:
        expenses = [int(r) for r in f.readlines()]

    print("Part 1: {}".format(part1(expenses)))
    print("Part 2: {}".format(part2(expenses)))
