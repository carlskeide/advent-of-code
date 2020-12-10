# coding=utf-8
from . import load_input

from collections import Counter
from itertools import combinations
from multiprocessing.dummy import Pool


def jolt_differences(adapters, output=None):
    jolts = [0] + sorted(adapters) + [output or max(adapters) + 3]
    return (jolts[i] - jolts[(i - 1)] for i in range(1, len(jolts)))


def all_arrangements(adapters):
    for i in range(1, len(adapters) + 1):
        for candidate in combinations(adapters, i):
            yield candidate


def valid_arrangements(adapters):
    output = max(adapters) + 3
    arrangements = all_arrangements(adapters)

    def is_valid(adapters):
        return all(jolt < 4 for jolt in jolt_differences(adapters, output))

    print("starting count")
    # return sum(is_valid(candidate) for candidate in arrangements)

    pool = Pool(8)
    num_valid = 0
    for result in pool.imap_unordered(is_valid, arrangements):
        num_valid += 1

    return num_valid


if __name__ == "__main__":
    task_input = [int(line) for line in load_input(day=10, group_lines=False)]

    differences = jolt_differences(task_input)
    counter = dict(Counter(differences))
    print(f"Part 1: {counter[1] * counter[3]}")

    part2 = ""
    print(f"Part 2: {part2}")
