# coding=utf-8
from itertools import chain
from . import load_input

SIMPLE = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}


def infer_basic(segments):
    return (SIMPLE.get(len(segment), None) for segment in segments)


def find_key(patterns):
    parsed = [(len(pattern), frozenset(pattern)) for pattern in patterns]
    key = {SIMPLE[plen]: pset for plen, pset in parsed if plen in SIMPLE}
    for plen, pset in parsed:
        if plen == 5:
            if pset.issuperset(key[1]):
                key[3] = pset

            elif pset.issuperset(key[4] - key[1]):
                key[5] = pset

            else:
                key[2] = pset

        elif plen == 6:
            if not pset.issuperset(key[1]):
                key[6] = pset

            elif pset.issuperset(key[4]):
                key[9] = pset

            else:
                key[0] = pset

    return key


def decode(key, patterns):
    revkey = {v: k for k, v in key.items()}
    return int("".join(str(revkey[frozenset(s)]) for s in patterns))


if __name__ == "__main__":
    task_input = load_input(day=8, group_lines=False)
    segments = [
        tuple(part.split() for part in line.split(' | '))
        for line in task_input
    ]

    inferred = chain.from_iterable(infer_basic(out) for _, out in segments)
    part1 = len(list(filter(None, inferred)))
    print(f"Part 1: {part1}")

    part2 = sum(decode(find_key(patterns), out) for patterns, out in segments)
    print(f"Part 2: {part2}")
