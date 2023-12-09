# coding=utf-8
from ..utils import load_input
from itertools import pairwise


def fill_recursive(stack: list[list[int]]) -> list[int]:
    delta = stack.pop()[-1]
    series = stack[-1]
    series.append(series[-1] + delta)
    if len(stack) == 1:
        return series
    else:
        return fill_recursive(stack)


def extrapolate(series: list[int]) -> int:
    stack = [series, ]
    while True:
        series = [b - a for a, b in pairwise(series)]
        stack.append(series)
        if set(series) == {0}:
            return fill_recursive(stack)[-1]


if __name__ == "__main__":
    task_input = load_input(year=2023, day=9, group_lines=False)
    parsed_input = [[int(i) for i in  line.split()] for line in task_input]

    part1 = sum(extrapolate(series) for series in parsed_input)
    print(f"Part 1: {part1}")

    part2 = sum(extrapolate(list(reversed(series))) for series in parsed_input)
    print(f"Part 2: {part2}")
