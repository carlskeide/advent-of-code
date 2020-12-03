#!/usr/bin/env python3
# coding=utf-8

# Starting at the top-left corner of your map and following a slope of
# right 3 and down 1, how many trees would you encounter?

from math import prod


def toboggan(terrain, delta_x, delta_y):
    col = 0
    for row in terrain[::delta_y]:
        yield row[col % len(row)] == "#"
        col += delta_x


if __name__ == "__main__":
    with open("./task3.input") as f:
        terrain = [line.strip() for line in f.readlines() if line]

    print(f"Part 1: hit {sum(toboggan(terrain, delta_x=3, delta_y=1))} trees")

    trees_hit = []
    for delta_x, delta_y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees_hit.append(sum(toboggan(terrain, delta_x, delta_y)))
        print(f"Vector {delta_x}, {delta_y}: hit {trees_hit[-1]} trees")

    print(f"Path 2: result {prod(trees_hit)}")
