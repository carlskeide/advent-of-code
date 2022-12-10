# coding=utf-8
from itertools import chain, repeat
from collections import Counter
from ..utils import load_input


def make_range(start, stop):
    if start < stop:
        return range(start, stop + 1)

    elif start > stop:
        return range(start, stop - 1, -1)

    else:
        return repeat(start)


def make_lines(charter, diagonals=False):
    for text in charter:
        pos1, pos2 = text.split("->")
        x1, y1, x2, y2 = map(int, pos1.split(",") + pos2.split(","))
        if (x1 != x2 and y1 != y2) and not diagonals:
            continue

        yield list(f"{x},{y}" for x, y in zip(make_range(x1, x2),
                                              make_range(y1, y2)))



def overlap(lines):
    count = Counter(chain.from_iterable(lines))
    return sum(v > 1 for v in count.values())


if __name__ == "__main__":
    task_input = load_input(year=2021, day=5, group_lines=False)

    straight_lines = make_lines(task_input)
    part1 = overlap(straight_lines)
    print(f"Part 1: {part1}")

    all_lines = make_lines(task_input, diagonals=True)
    part2 = overlap(all_lines)
    print(f"Part 2: {part2}")
