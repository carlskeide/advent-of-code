# coding=utf-8
from ..utils import load_input


def most_common(items):
    pivot = len(items) / 2
    num_ones = sum(item == "1" for item in items)
    return "1" if num_ones >= pivot else "0"


def get_gamma(codes):
    return "".join(
        most_common([code[pos] for code in codes])
        for pos in range(len(codes[0]))
    )


def to_epsilon(bin_string):
    return "".join(str(int(s == "0")) for s in bin_string)


def filter_common(codes, invert=False):
    remaining = codes
    for pos in range(len(codes[0])):
        match = most_common([code[pos] for code in remaining])
        if invert:
            match = "0" if match == "1" else "1"

        remaining = [code for code in remaining if code[pos] == match]
        if len(remaining) == 1:
            return remaining[0]


if __name__ == "__main__":
    task_input = load_input(year=2021, day=3, group_lines=False)

    gamma = get_gamma(task_input)
    epsilon = to_epsilon(gamma)
    print(f"Gamma: {gamma}, epsilon: {epsilon}")

    part1 = int(gamma, 2) * int(epsilon, 2)
    print(f"Part 1: {part1}")

    o2 = filter_common(task_input)
    co2 = filter_common(task_input, invert=True)
    print(f"O2: {o2}, CO2: {co2}")

    part2 = int(o2, 2) * int(co2, 2)
    print(f"Part 2: {part2}")
