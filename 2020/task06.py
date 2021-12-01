# coding=utf-8
from . import load_input

from functools import reduce


def distinct_answers(answers):
    return set(answers.replace('\n', ''))


def common_answers(answers):
    return reduce(set.intersection, map(set, answers.splitlines()))


if __name__ == "__main__":
    answers = load_input(day=6, group_lines=True)

    print(f"Part 1: {sum(map(len, map(distinct_answers, answers)))}")
    print(f"Part 2: {sum(map(len, map(common_answers, answers)))}")
