#!/usr/bin/env python3
# coding=utf-8

# Starting at the top-left corner of your map and following a slope of
# right 3 and down 1, how many trees would you encounter?

from math import prod


def toboggan(terrain, delta_x, delta_y):
    x, y = 0, 0

    while True:
        try:
            row = terrain[y]
        except IndexError:
            return

        yield row[x] == "#"
        x += delta_x
        y += delta_y


if __name__ == "__main__":
    with open("./task3.input") as f:
        terrain = [line.strip() * 255 for line in f.readlines() if line]

    steps = list(toboggan(terrain, delta_x=3, delta_y=1))
    print(f"Part 1: hit {sum(steps)} trees out of {len(steps)} steps")

    print("Part 2:")
    trees_hit = []
    for delta_x, delta_y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees_hit.append(sum(toboggan(terrain, delta_x, delta_y)))
        print(f"Vector {delta_x}, {delta_y}: hit {trees_hit[-1]} trees")

    print(f"Result: {prod(trees_hit)}")
