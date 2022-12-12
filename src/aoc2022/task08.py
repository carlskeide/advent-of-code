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


def score(heightmap, x, y):
    tree = heightmap[y][x]
    row = heightmap[y]
    col = [line[x] for line in heightmap]
    vectors = (
        reversed(row[:x]),
        row[x + 1:],
        reversed(col[:y]),
        col[y + 1:]
    )

    score = 1
    for vector in vectors:
        vector_score = 0
        for height in vector:
            vector_score += 1
            if height >= tree:
                break

        if vector_score:
            score *= vector_score

    return score


if __name__ == "__main__":
    heightmap = [
        [int(c) for c in line]
        for line in load_input(year=2022, day=8)
    ]

    part1 = visible_trees(heightmap)
    print(f"Part 1: {part1}")

    part2 = max(
        score(heightmap, x, y)
        for y in range(len(heightmap))
        for x in range(len(heightmap[0]))
    )
    print(f"Part 2: {part2}")
