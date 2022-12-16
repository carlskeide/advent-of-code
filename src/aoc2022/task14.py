# coding=utf-8
from itertools import pairwise

from ..utils import load_input
from ..models import SparseGrid


class Cave(SparseGrid):
    entry_pos = (500, 0)

    def __init__(self, paths):
        super().__init__()

        for path in paths:
            for start, stop in pairwise(path):
                start_x, start_y = start
                stop_x, stop_y = stop
                if start_x == stop_x:
                    for y in range(min(start_y, stop_y), max(start_y, stop_y) + 1):
                        self[(start_x, y)] = "#"
                else:
                    for x in range(min(start_x, stop_x), max(start_x, stop_x) + 1):
                        self[(x, start_y)] = "#"

        self[self.entry_pos] = "+"
        self.edge = max({y for _, y in self})

    def __str__(self):
        return "\n".join(reversed(super().__str__().splitlines()))

    def run_until_stable(self):
        grains = 0
        while True:
            try:
                self.drop_grain()

            except StopIteration:
                break

            else:
                grains += 1

        return grains

    def drop_grain(self):
        grain_x, grain_y = self.entry_pos

        while True:
            if self.get((grain_x, grain_y + 1)):
                if self.get((grain_x - 1, grain_y + 1)):
                    if self.get((grain_x + 1, grain_y + 1)):
                        break

                    else:
                        grain_x += 1
                        grain_y += 1

                else:
                    grain_x -= 1
                    grain_y += 1

            else:
                grain_y += 1

            if grain_y > self.edge:
                raise StopIteration()

        self[(grain_x, grain_y)] = "o"


class FlooredCave(Cave):

    def get(self, position, default=None):
        if position[1] == self.edge + 2:
            return "#"

        else:
            return super().get(position, default)


    def drop_grain(self):
        if self[self.entry_pos] == "o":
            raise StopIteration()

        grain_x, grain_y = self.entry_pos

        while True:
            if self.get((grain_x, grain_y + 1)):
                if self.get((grain_x - 1, grain_y + 1)):
                    if self.get((grain_x + 1, grain_y + 1)):
                        break

                    else:
                        grain_x += 1
                        grain_y += 1

                else:
                    grain_x -= 1
                    grain_y += 1

            else:
                grain_y += 1

        self[(grain_x, grain_y)] = "o"

if __name__ == "__main__":
    paths = [
        [eval(pos) for pos in path.split(' -> ')]
        for path in load_input(year=2022, day=14)
    ]

    part1 = Cave(paths).run_until_stable()
    print(f"Part 1: {part1}")

    part2 = FlooredCave(paths).run_until_stable()
    print(f"Part 2: {part2}")
