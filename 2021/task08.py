# coding=utf-8
from itertools import chain
from collections import Counter
from . import load_input

SIMPLE = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}


def infer_basic(segments):
    return (SIMPLE.get(len(segment), None) for segment in segments)


if __name__ == "__main__":
    task_input = load_input(day=8, group_lines=False)
    segments = [
        (part.split() for part in line.split(' | '))
        for line in task_input
    ]

    inferred = chain.from_iterable(infer_basic(s) for _, s in segments)
    part1 = len(list(filter(None, inferred)))
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
