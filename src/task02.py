# coding=utf-8
from . import load_input

import re
from collections import Counter


def policy_num_letter(pol, pwd):
    letters = Counter(pwd)
    r_min, r_max, letter = re.match(r"^(\d+)-(\d+) *([a-z])", pol).groups()

    return (int(r_min) <= letters[letter] <= int(r_max))


def policy_letter_pos(pol, pwd):
    pos_1, pos_2, letter = re.match(r"^(\d+)-(\d+) *([a-z])", pol).groups()

    return (pwd[int(pos_1) - 1] == letter) != (pwd[int(pos_2) - 1] == letter)


if __name__ == "__main__":
    passwords = [
        re.match(r"^(.*):\s?(\w+)", line).groups()
        for line in load_input(day=2)
    ]

    print(f"Part 1: {sum(policy_num_letter(*sig) for sig in passwords)}")
    print(f"Part 2: {sum(policy_letter_pos(*sig) for sig in passwords)}")
