# coding=utf-8
from ..utils import load_input


def visible_trees(heightmap):
    width = len(heightmap[0])
    height = len(heightmap)
    border = width * 2 + height * 2 - 4

    inner = 0
    for y in range(1, width - 1):
        for x in range(1, height -1):
            tree = heightmap[y][x]
            row = heightmap[y]
            col = [line[x] for line in heightmap]

            inner += min(
                max(row[:x]),
                max(row[x + 1:]),
                max(col[:y]),
                max(col[y + 1:])
            ) < tree

    return border + inner

if __name__ == "__main__":
    heightmap = [
        [int(c) for c in line]
        for line in load_input(year=2022, day=8)
    ]

    part1 = visible_trees(heightmap)
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
