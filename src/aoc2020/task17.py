# coding=utf-8
from ..utils import load_input

from collections import defaultdict as dd


class GameOfCubes:
    def __init__(self, seed):
        self.space = dd(lambda: dd(lambda: dd(int)))

        offset = len(seed) // 2
        for y, row in enumerate(seed):
            for x, cube in enumerate(row):
                if cube == "#":
                    self.space[0][y - offset][x - offset] = 1

    def step(self):
        prev_space = self.space

        coords = (
            (z, y, x)
            for z in prev_space
            for y in prev_space[z]
            for x in prev_space[z][y]
        )

        expanded = {
            (zz, yy, xx)
            for z, y, x in coords
            for zz in range(z - 1, z + 2)
            for yy in range(y - 1, y + 2)
            for xx in range(x - 1, x + 2)
        }

        self.space = dd(lambda: dd(lambda: dd(int)))
        for z, y, x in expanded:
            self.space[z][y][x] = self.calcube(prev_space, z, y, x)

    def calcube(self, prev_space, z, y, x):
        n = 0
        cube = prev_space[z][y][x]
        for zz in range(z - 1, z + 2):
            for yy in range(y - 1, y + 2):
                for xx in range(x - 1, x + 2):
                    if (zz, yy, xx) != (z, y, x):
                        n += prev_space[zz][yy][xx]

        if cube == 1 and n not in (2, 3):
            cube = 0

        elif cube == 0 and n == 3:
            cube = 1

        return cube

    def run(self, steps=6):
        for i in range(steps):
            self.step()

    @property
    def active(self):
        return sum(
            y
            for z in self.space.values()
            for x in z.values()
            for y in x.values()
        )


class GameOfHyperCubes:
    def __init__(self, seed):
        self.space = dd(lambda: dd(lambda: dd(lambda: dd(int))))

        offset = len(seed) // 2
        for y, row in enumerate(seed):
            for x, cube in enumerate(row):
                if cube == "#":
                    self.space[0][0][y - offset][x - offset] = 1

    def step(self):
        prev_space = self.space

        coords = (
            (w, z, y, x)
            for w in prev_space
            for z in prev_space[w]
            for y in prev_space[w][z]
            for x in prev_space[w][z][y]
        )

        expanded = {
            (ww, zz, yy, xx)
            for w, z, y, x in coords
            for ww in range(w - 1, w + 2)
            for zz in range(z - 1, z + 2)
            for yy in range(y - 1, y + 2)
            for xx in range(x - 1, x + 2)
        }

        self.space = dd(lambda: dd(lambda: dd(lambda: dd(int))))
        for w, z, y, x in expanded:
            self.space[w][z][y][x] = self.calcube(prev_space, w, z, y, x)

    def calcube(self, prev_space, w, z, y, x):
        n = 0
        cube = prev_space[w][z][y][x]
        for ww in range(w - 1, w + 2):
            for zz in range(z - 1, z + 2):
                for yy in range(y - 1, y + 2):
                    for xx in range(x - 1, x + 2):
                        if (ww, zz, yy, xx) != (w, z, y, x):
                            n += prev_space[ww][zz][yy][xx]

        if cube == 1 and n not in (2, 3):
            cube = 0

        elif cube == 0 and n == 3:
            cube = 1

        return cube

    def run(self, steps=6):
        for i in range(steps):
            self.step()

    @property
    def active(self):
        return sum(
            y
            for w in self.space.values()
            for z in w.values()
            for x in z.values()
            for y in x.values()
        )


if __name__ == "__main__":
    task_input = load_input(year=2020, day=17)

    game = GameOfCubes(task_input)
    game.run(steps=6)
    print(f"Part 1: {game.active}")

    game = GameOfHyperCubes(task_input)
    game.run(steps=6)
    print(f"Part 2: {game.active}")
