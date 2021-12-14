# coding=utf-8
from itertools import tee
from collections import Counter
from functools import lru_cache

from . import load_input


def pairwise(iterable):
    """ Included in python >= 3.10 """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


class Polymer:
    def __init__(self, seed, rules):
        self.state = tuple(seed)
        self.rules = {
            tuple(pair): insert
            for pair, insert in (
                rule.split(" -> ") for rule in rules
            )
        }

    def polymerize(self, steps=1):
        counts = Counter()
        for a, b in pairwise(self.state):
            counts.update(self._expand(a, b, depth=steps))

        counts.update(b)
        return counts

    @lru_cache(maxsize=None)
    def _expand(self, a, b, depth):
        depth -= 1

        counts = Counter()
        if not depth:
            counts.update(a)

        if (a, b) in self.rules:
            new = self.rules[(a, b)]

            if not depth:
                counts.update(new)

            else:
                counts.update(self._expand(a, new, depth))
                counts.update(self._expand(new, b, depth))

        return counts

if __name__ == "__main__":
    seed, rules = load_input(day=14, group_lines=True)
    polymer = Polymer(seed, rules.splitlines())

    count = polymer.polymerize(10).most_common()
    print(f"Part 1: {count[0][1] - count[-1][1]}")

    count = polymer.polymerize(40).most_common()
    print(f"Part 2: {count[0][1] - count[-1][1]}")
