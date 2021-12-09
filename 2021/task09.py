# coding=utf-8
from . import load_input


def make_map(charter):
    return [list(map(int, s)) for s in charter]


def find_lows(heightmap):
    len_y = len(heightmap)
    len_x = len(heightmap[0])
    for y in range(len_y):
        for x in range(len_x):
            point = heightmap[y][x]
            others = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
            for other_x, other_y in others:
                if not (0 <= other_x < len_x and 0 <= other_y < len_y):
                    continue

                other = heightmap[other_y][other_x]
                if point >= other:
                    break

            else:
                yield point


if __name__ == "__main__":
    task_input = load_input(day=9, group_lines=False)
    heightmap = make_map(task_input)

    lows = list(find_lows(heightmap))
    part1 = sum(lows) + len(lows)
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
