#!/usr/bin/env python3
#
# find the two entries that sum to 2020 and then multiply those two numbers together.
#

INPUT_DATA_URL = "https://adventofcode.com/2020/day/1/input"

with open("./task1.input") as f:
    expenses = [int(r) for r in f.readlines()]

for item in expenses:
    needle = abs(item - 2020)
    if needle in expenses:
        print(f"{item} * {needle} = {item * needle}")
        break

else:
    print("No match!")
