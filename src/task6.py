# coding=utf-8
from . import load_input

from functools import reduce


if __name__ == "__main__":
    answers = load_input(day=6, group_lines=True)

    distinct_answers = [len(set(group.replace('\n', ''))) for group in answers]
    print(f"Part 1: {sum(distinct_answers)}")

    common_answers = [
        reduce(set.intersection, map(set, group.splitlines()))
        for group in answers
    ]
    print(f"Part 2: {sum(len(common) for common in common_answers)}")
