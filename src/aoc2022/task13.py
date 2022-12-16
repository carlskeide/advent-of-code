# coding=utf-8
from itertools import chain
from functools import cmp_to_key

from ..utils import load_input


def is_sorted(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None

        else:
            return left < right

    else:
        if isinstance(left, int):
            left = [left, ]

        if isinstance(right, int):
            right = [right, ]

        for i in range(min(len(left), len(right))):
            res = is_sorted(left[i], right[i])
            if res is not None:
                return res

        else:
            if len(left) < len(right):
                return True

            elif len(left) > len(right):
                return False

            else:
                return None


if __name__ == "__main__":
    pairs = [
        tuple(eval(line) for line in pair.splitlines())
        for pair in load_input(year=2022, day=13, group_lines=True)
    ]

    part1 = {
        i: is_sorted(*pair)
        for i, pair in enumerate(pairs, start=1)
    }
    print(f"Part 1: {sum(k for k, v in part1.items() if v)}")

    packets = list(chain.from_iterable(pairs)) + [[[2]], [[6]]]
    packets.sort(key=cmp_to_key(lambda left, right: -1 if is_sorted(left, right) else 1))

    print(f"Part 2: {(packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)}")
