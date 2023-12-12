# coding=utf-8
from typing import Iterator
from itertools import combinations
from ..utils import load_input
from ..models import SparseGrid, Charter


class Universe(SparseGrid):
    def __init__(self, charter: Charter) -> None:
        self.state = {
            (x, y): val
            for y, line in enumerate(reversed(charter))
            for x, val in enumerate(line)
            if val == "#"
        }

    def expand(self, factor: int = 2) -> None:
        min_edge, max_edge = self.size

        occupied_rows = {y for _, y in self}
        occupied_cols = {x for x, _ in self}

        for row in range(max_edge[0], min_edge[0] - 1, -1):
            if row not in occupied_rows:
                self.state = {
                    (x, y if y < row else y + factor - 1): val
                    for (x, y), val in self.state.items()
                }

        for col in range(max_edge[1], min_edge[1] - 1, -1):
            if col not in occupied_cols:
                self.state = {
                    (x if x < col else x + factor - 1, y): val
                    for (x, y), val in self.state.items()
                }

    def distances(self) -> Iterator[int]:
        for a, b in combinations(self, r=2):
            yield abs(b[0] - a[0]) + abs(b[1] - a[1])


if __name__ == "__main__":
    task_input = load_input(year=2023, day=11, group_lines=False)
    universe = Universe(task_input)
    universe.expand()

    part1 = sum(universe.distances())
    print(f"Part 1: {part1}")

    universe = Universe(task_input)
    universe.expand(1000000)
    part2 = sum(universe.distances())
    print(f"Part 2: {part2}")
