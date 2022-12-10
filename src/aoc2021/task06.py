# coding=utf-8
from ..utils import load_input
from collections import Counter


def simulate(fishes, days):
    school = Counter(fishes)
    for _ in range(days):
        spawm = school.get(0, 0)
        for i in range(8):
            school[i] = school.get(i + 1, 0)

        school[6] += spawm
        school[8] = spawm

    return sum(school.values())


if __name__ == "__main__":
    task_input = load_input(year=2021, day=6, group_lines=False)
    school = [int(s) for s in task_input[0].split(",")]

    part1 = simulate(school, days=80)
    print(f"Part 1: {part1}")

    part2 = simulate(school, days=256)
    print(f"Part 2: {part2}")
