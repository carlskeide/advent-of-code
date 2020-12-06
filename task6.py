#!/usr/bin/env python3
# coding=utf-8

# Duplicate answers to the same question don't count extra; each question
# counts at most once

from functools import reduce


if __name__ == "__main__":
    with open("./task6.input") as f:
        answers = f.read().split("\n\n")

    distinct_answers = [len(set(group.replace('\n', ''))) for group in answers]
    print(f"Part 1: {sum(distinct_answers)}")

    common_answers = [
        reduce(set.intersection, map(set, group.splitlines()))
        for group in answers
    ]
    print(f"Part 2: {sum(len(common) for common in common_answers)}")
