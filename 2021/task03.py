# coding=utf-8
from . import load_input


def get_gamma(codes):
    pivot = len(codes) // 2
    return "".join(
        str(int(sum(int(code[pos]) for code in codes) > pivot))
        for pos in range(len(codes[0]))
    )


def to_epsilon(bin_string):
    return "".join(str(int(s == "0")) for s in bin_string)


if __name__ == "__main__":
    task_input = load_input(day=3, group_lines=False)

    gamma = get_gamma(task_input)
    epsilon = to_epsilon(gamma)
    print(f"Gamma: {gamma}, epsilon: {epsilon}")

    part1 = int(gamma, 2) * int(epsilon, 2)
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
