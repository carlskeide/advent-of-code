#!/usr/bin/env python3
#
# Each line gives the password policy and then the password.
# The password policy indicates the lowest and highest number of times
# a given letter must appear for the password to be valid. For example,
# 1-3 a means that the password must contain a at least 1 time and at most
# 3 times.

import re
from collections import Counter


def task2(pol, pwd):
    letters = Counter(pwd)
    r_min, r_max, letter = re.match(r"^(\d+)-(\d+) *([a-z])", pol).groups()

    return (int(r_min) <= letters[letter] <= int(r_max))


if __name__ == "__main__":
    with open("./task2.input") as f:
        passwords = [
            re.match(r"^(.*):\s?(\w+)", line).groups()
            for line in f.readlines() if line
        ]

    valid_passwords = [task2(*sig) for sig in passwords]
    print(f"Task 2: {sum(valid_passwords)} of {len(passwords)} are valid")
