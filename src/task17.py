# coding=utf-8
from . import load_input


class GameOfCubes:
    size = 14

    def __init__(self, seed):
        axis = list(range(self.size * -1, self.size + 1))
        self.space = {
            z: {
                y: {
                    x: "." for x in axis
                } for y in axis
            } for z in axis
        }

        for y, row in enumerate(seed):
            for x, cube in enumerate(row):
                if cube == "#":
                    self.space[0][y][x] = cube

    def step(self):
        new_space = {}
        for z in self.space:
            new_space[z] = {}
            for y in self.space[z]:
                new_space[z][y] = {}
                for x in self.space[z][y]:
                    if max(map(abs, (z, y, x))) == self.size:
                        cube = "."

                    else:
                        cube = self.space[z][y][x]
                        neighbors = self.neighbors(z, y, x)
                        if cube == "#" and neighbors not in (2, 3):
                            cube = "."
                        elif cube == "." and neighbors == 3:
                            cube = "#"

                    new_space[z][y][x] = cube

        self.space = new_space

    def neighbors(self, z, y, x):
        count = 0
        for zz in range(z - 1, z + 2):
            for yy in range(y - 1, y + 2):
                for xx in range(x - 1, x + 2):
                    if (zz, yy, xx) == (z, y, x):
                        continue

                    else:
                        count += self.space[zz][yy][xx] == "#"

        return count

    def run(self, steps=6):
        for i in range(steps):
            self.step()

    @property
    def active(self):
        return sum(
            y == "#"
            for z in self.space.values()
            for x in z.values()
            for y in x.values()
        )


if __name__ == "__main__":
    task_input = load_input(day=17)

    game = GameOfCubes(task_input)
    game.run(steps=6)
    print(f"Part 1: {game.active}")

    # part2 = ""
    # print(f"Part 2: {part2}")
