# coding=utf-8
from ..utils import load_input

from collections import Counter
from itertools import groupby


def jolt_differences(adapters):
    jolts = [0] + sorted(adapters) + [max(adapters) + 3]
    return [jolts[i] - jolts[(i - 1)] for i in range(1, len(jolts))]


def valid_arrangements(jolts):
    total = 1
    for num in (len(list(group)) for n, group in groupby(jolts) if n < 3):
        paths = 2 ** (num - 1)

        if num > 3:
            paths -= 1

        total *= paths

    return total


if __name__ == "__main__":
    task_input = [int(line) for line in load_input(year=2020, day=10, group_lines=False)]

    differences = jolt_differences(task_input)
    counter = dict(Counter(differences))
    print(f"Part 1: {counter[1] * counter[3]}")

    paths = valid_arrangements(differences)
    assert paths == 48358655787008
    print(f"Part 2: {paths}")
