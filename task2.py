#!/usr/bin/env python3
#
# Each line gives the password policy and then the password.
# The password policy indicates the lowest and highest number of times
# a given letter must appear for the password to be valid. For example,
# 1-3 a means that the password must contain a at least 1 time and at most
# 3 times.

import re
from collections import Counter


def part1(pol, pwd):
    letters = Counter(pwd)
    r_min, r_max, letter = re.match(r"^(\d+)-(\d+) *([a-z])", pol).groups()

    return (int(r_min) <= letters[letter] <= int(r_max))


# Each policy actually describes two positions in the password, where 1 means
# the first character, 2 means the second character, and so on.
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
# Exactly one of these positions must contain the given letter.
# Other occurrences of the letter are irrelevant for the purposes of
# policy enforcement.

def part2(pol, pwd):
    pos_1, pos_2, letter = re.match(r"^(\d+)-(\d+) *([a-z])", pol).groups()

    return (pwd[int(pos_1) - 1] == letter) != (pwd[int(pos_2) - 1] == letter)


if __name__ == "__main__":
    with open("./task2.input") as f:
        passwords = [
            re.match(r"^(.*):\s?(\w+)", line).groups()
            for line in f.readlines() if line
        ]

    valid_part1 = [part1(*sig) for sig in passwords]
    print(f"Part 1: {sum(valid_part1)} of {len(passwords)} are valid")

    valid_part2 = [part2(*sig) for sig in passwords]
    print(f"Part 2: {sum(valid_part2)} of {len(passwords)} are valid")
