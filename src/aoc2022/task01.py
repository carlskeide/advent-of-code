# coding=utf-8
from ..utils import load_input


def most_calories(calories, num):
    return sorted(sum(group) for group in calories)[-num:]


if __name__ == "__main__":
    calories = [
        [int(line) for line in group.splitlines()]
        for group in load_input(year=2022, day=1, group_lines=True)
    ]

    part1 = sum(most_calories(calories, num=1))
    print(f"Part 1: {part1}")

    part2 = sum(most_calories(calories, num=3))
    print(f"Part 2: {part2}")
