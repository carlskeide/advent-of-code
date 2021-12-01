# coding=utf-8
from . import load_input

def num_increases(depths):
    return sum(depths[i] > depths[i - 1] for i in range(1, len(depths)))

def sliding_increases(depths):
    groups = [sum(depths[i:i + 3]) for i in range(len(depths) - 2)]
    return num_increases(groups)

if __name__ == "__main__":
    task_input = load_input(day=1, group_lines=False)
    depths = [int(i) for i in task_input]

    part1 = num_increases(depths)
    print(f"Part 1: {part1}")

    part2 = sliding_increases(depths)
    print(f"Part 2: {part2}")
