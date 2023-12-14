# coding=utf-8
from typing import Any
from itertools import chain
from ..utils import load_input
from ..models import SimpleGrid


def find_reflection(grid: list[list[Any]], fuzzy: bool, skip: int) -> int:
    size = len(grid)
    for i in (i for i in range(1, size) if i != skip):
        window = min(i, size - i)
        diffs = sum(
            pair[0] != pair[1] for pair in zip(
                chain(*grid[i - 1::-1][:window]),
                chain(*grid[i:][:window])
            )
        )
        if diffs <= int(fuzzy):
            return i


class MirrorMap(SimpleGrid):
    def __init__(self, charter):
        super().__init__(charter)
        self.matched = {"x": 0, "y": 0}

    def value(self, fuzzy=False):
        if (y:= find_reflection(self.state, fuzzy, self.matched["y"])):
            self.matched["y"] = y
            return y * 100

        cols = list(self.columns())
        if (x := find_reflection(cols, fuzzy, self.matched["x"])):
            self.matched["x"] = x
            return x

        raise ValueError("No mirror found!")


if __name__ == "__main__":
    task_input = load_input(year=2023, day=13, group_lines=True)
    maps = [
        MirrorMap(group.splitlines()) for group in task_input
    ]

    part1 = sum(mmap.value() for mmap in maps)
    print(f"Part 1: {part1}")

    part2 = sum(mmap.value(fuzzy=True) for mmap in maps)
    print(f"Part 2: {part2}")
