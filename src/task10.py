# coding=utf-8
from . import load_input

from collections import Counter


def jolt_differences(adapters, output=None):
    jolts = [0] + sorted(adapters) + [output or max(adapters) + 3]
    return (jolts[i] - jolts[(i - 1)] for i in range(1, len(jolts)))


def traverse(cur, nodes):
    valid = 0

    if cur < 4:
        valid += 1

    for i in range(len(nodes)):
        forward = nodes.copy()
        next_node = forward.pop(i)

        if 0 < (cur - next_node) < 4:
            valid += traverse(cur=next_node, nodes=forward)

    return valid


def valid_arrangements(adapters):
    output = max(adapters) + 3
    valid_paths = traverse(output, adapters)
    return valid_paths


if __name__ == "__main__":
    task_input = [int(line) for line in load_input(day=10, group_lines=False)]

    differences = jolt_differences(task_input)
    counter = dict(Counter(differences))
    print(f"Part 1: {counter[1] * counter[3]}")

    print(f"Part 2: {valid_arrangements(task_input)}")
