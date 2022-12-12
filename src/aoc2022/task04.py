# coding=utf-8
from ..utils import load_input


def parse_assignment(assignment):
    return (
        set(range(int(start), int(stop) + 1))
        for start, stop in (line.split("-") for line in assignment)
    )


def is_redundant(assignment):
    a, b = parse_assignment(assignment)
    return (a.issuperset(b) or a.issubset(b))


def has_overlap(assignment):
    a, b = parse_assignment(assignment)
    return not a.isdisjoint(b)


if __name__ == "__main__":
    assignments = [
        line.split(',') for line in load_input(year=2022, day=4)
    ]

    part1 = (is_redundant(assignment) for assignment in assignments)
    print(f"Part 1: {sum(part1)}")

    part2 = (has_overlap(assignment) for assignment in assignments)
    print(f"Part 2: {sum(part2)}")
