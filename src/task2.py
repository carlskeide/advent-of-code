# coding=utf-8
from . import load_input

import re
from collections import Counter


def part1(pol, pwd):
    letters = Counter(pwd)
    r_min, r_max, letter = re.match(r"^(\d+)-(\d+) *([a-z])", pol).groups()

    return (int(r_min) <= letters[letter] <= int(r_max))


def part2(pol, pwd):
    pos_1, pos_2, letter = re.match(r"^(\d+)-(\d+) *([a-z])", pol).groups()

    return (pwd[int(pos_1) - 1] == letter) != (pwd[int(pos_2) - 1] == letter)


if __name__ == "__main__":
    passwords = [
        re.match(r"^(.*):\s?(\w+)", line).groups()
        for line in load_input(day=2)
    ]

    valid_part1 = [part1(*sig) for sig in passwords]
    print(f"Part 1: {sum(valid_part1)} of {len(passwords)} are valid")

    valid_part2 = [part2(*sig) for sig in passwords]
    print(f"Part 2: {sum(valid_part2)} of {len(passwords)} are valid")
