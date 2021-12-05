# coding=utf-8
from itertools import chain
from collections import Counter
from . import load_input

def make_line(text):
    pos1, pos2 = text.split("->")
    x1, y1, x2, y2 = map(int, pos1.split(",") + pos2.split(","))
    if y1 == y2:
        start, stop = sorted([x1, x2])
        return (f"{x},{y1}" for x in range(start, stop + 1))

    if x1 == x2:
        start, stop = sorted([y1, y2])
        return (f"{x1},{y}" for y in range(start, stop + 1))

    else:
        return None


def overlap(lines):
    count = Counter(chain.from_iterable(lines))
    return sum(v > 1 for v in count.values())


if __name__ == "__main__":
    task_input = load_input(day=5, group_lines=False)
    straight_lines = filter(None, map(make_line, task_input))
    part1 = overlap(straight_lines)
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
