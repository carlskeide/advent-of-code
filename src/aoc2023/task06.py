# coding=utf-8
from functools import reduce
import operator
from ..utils import load_input


def winning_times(ms, mm):
    return sum((i * (ms - i) > mm) for i in range(1, ms))


if __name__ == "__main__":
    task_input = load_input(year=2023, day=6, group_lines=False)
    races = [
        (int(ms), int(mm)) for ms, mm in
        zip(*(line.split(":")[-1].split() for line in task_input))
    ]

    part1 = reduce(operator.mul, (winning_times(ms, mm) for ms, mm in races))
    print(f"Part 1: {part1}")

    ms, mm = (int(line.split(":")[-1].replace(" ", "")) for line in task_input)
    part2 = winning_times(ms, mm)
    print(f"Part 2: {part2}")
