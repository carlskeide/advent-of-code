# coding=utf-8
from . import load_input


def move_cups(cups):
    first, *other = cups
    moved = [other.pop(0) for _ in range(3)]
    target = first - 1
    while target not in other:
        target = target - 1 if target > min(cups) else max(cups)

    ix = other.index(target) + 1
    return other[:ix] + moved + other[ix:] + [first]


def cformat(cups):
    ix = cups.index(1)
    return "".join(str(c) for c in cups[ix + 1:] + cups[:ix])


if __name__ == "__main__":
    task_input = load_input(day=23)
    cups = [int(n) for n in task_input[0]]

    for _ in range(100):
        cups = move_cups(cups)

    print(f"Part 1: {cformat(cups)}")

    many_cups = [int(n) for n in task_input[0]]
    many_cups += list(range(max(many_cups) + 1, 1000001))

    for _ in range(1000):
        many_cups = move_cups(many_cups)

    ix = many_cups.index(1)
    print(f"Part 2: {ix} -> {many_cups[ix:ix + 3]}")
