# coding=utf-8
from ..utils import load_input

from collections import deque


def find_header(datastream, size):
    window = deque(maxlen=size)
    for pos, char in enumerate(datastream, start=1):
        window.append(char)
        if len(set(window)) == size:
            return pos


if __name__ == "__main__":
    datastream = load_input(year=2022, day=6)[0]

    part1 = find_header(datastream, 4)
    print(f"Part 1: {part1}")

    part2 = find_header(datastream, 14)
    print(f"Part 2: {part2}")
