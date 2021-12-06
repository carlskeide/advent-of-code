# coding=utf-8
from . import load_input


def simulate(fishes, days):
    for d in range(days):
        fishes = [i - 1 if i > 0 else 6 for i in fishes] + ([8] * fishes.count(0))

    return fishes


if __name__ == "__main__":
    task_input = load_input(day=6, group_lines=False)
    school = list(map(int, task_input[0].split(",")))

    part1 = len(simulate(school, days=80))
    print(f"Part 1: {part1}")

    # part2 = len(simulate(school, days=256))
    # print(f"Part 2: {part2}")
