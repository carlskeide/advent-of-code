# coding=utf-8
from collections import defaultdict
from operator import add, sub, mul, truediv

from ..utils import load_input

OPS = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv
}


def resolve_monkeys(monkeys):
    resolved = set()
    references = defaultdict(set)
    for name, val in monkeys.items():
        if isinstance(val, int):
            resolved.add(name)

        else:
            references[val[0]].add(name)
            references[val[2]].add(name)

    while references:
        for name in list(references.keys()):
            if name not in resolved:
                continue

            for link in references[name]:
                for i in (0,2):
                    if monkeys[link][i] == name:
                        monkeys[link][i] = monkeys[name]

            del references[name]

        for name in monkeys:
            if name in resolved:
                continue

            left, op, right = monkeys[name]
            if isinstance(left, str) or isinstance(right, str):
                continue

            monkeys[name] = OPS[op](left, right)
            resolved.add(name)


if __name__ == "__main__":
    monkeys = {
        name: int(val) if val.isnumeric() else val.split()
        for name, val in (
            line.split(": ") for line in load_input(year=2022, day=21)
        )
    }

    resolve_monkeys(monkeys)
    print(f"Part 1: {int(monkeys['root'])}")

    part2 = ""
    print(f"Part 2: {part2}")
