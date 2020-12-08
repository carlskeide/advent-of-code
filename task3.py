# coding=utf-8
from utils import load_input

from math import prod


def toboggan(terrain, delta_x, delta_y):
    col = 0
    for row in terrain[::delta_y]:
        yield row[col % len(row)] == "#"
        col += delta_x


if __name__ == "__main__":
    terrain = load_input(day=3)
    print(f"Part 1: hit {sum(toboggan(terrain, delta_x=3, delta_y=1))} trees")

    trees_hit = []
    for delta_x, delta_y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees_hit.append(sum(toboggan(terrain, delta_x, delta_y)))
        print(f"Vector {delta_x}, {delta_y}: hit {trees_hit[-1]} trees")

    print(f"Path 2: result {prod(trees_hit)}")
