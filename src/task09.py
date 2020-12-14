# coding=utf-8
from . import load_input

from itertools import combinations


def validate(data, number):
    return (number in map(sum, combinations(data, 2)))


def validate_list(data, preamble=25):
    for i, number in enumerate(data):
        if i < preamble:
            continue

        data_slice = data[i - preamble:i]
        if not validate(data_slice, number):
            raise ValueError(number)


def find_weakness(data, target):
    for i in range(len(data)):
        data_slice = []
        j = i
        while sum(data_slice) < target and j < len(data):
            j += 1
            data_slice = data[i:j]

        if sum(data_slice) == target:
            return data_slice


if __name__ == "__main__":
    task_input = [int(x) for x in load_input(day=9)]

    try:
        validate_list(task_input)

    except ValueError as e:
        invalid = e.args[0]

    print(f"Part 1: {invalid}")

    weakness = find_weakness(task_input, invalid)
    print(f"Part 2: {min(weakness) + max(weakness)}")
