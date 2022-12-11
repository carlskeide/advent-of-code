# coding=utf-8
from string import ascii_letters
from functools import reduce

from ..utils import load_input, grouper


def priority(item):
    return ascii_letters.index(item) + 1


def find_common(backpack):
    divider = len(backpack) // 2
    compartments = (set(backpack[:divider]), set(backpack[divider:]))
    common = compartments[0] & compartments[1]

    return next(iter(common))


def find_group(backpacks):
    common = reduce(
        set.intersection,
        (set(backpack) for backpack in backpacks)
    )

    return next(iter(common))


if __name__ == "__main__":
    backpacks = load_input(year=2022, day=3, group_lines=False)

    part1 = [priority(find_common(backpack)) for backpack in backpacks]
    print(f"Part 1: {sum(part1)}")

    part2 = [priority(find_group(elfs)) for elfs in grouper(backpacks, 3)]
    print(f"Part 2: {sum(part2)}")
