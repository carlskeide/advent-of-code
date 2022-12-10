# coding=utf-8
from copy import deepcopy

from ..utils import load_input
from ..models import SimpleGrid


class GameOfCucumbers(SimpleGrid):
    def run_until_stable(self):
        steps = 1
        while self.step(">") + self.step("v"):
            steps += 1

        return steps

    def step(self, kind):
        to_move = []
        for pos in self:
            x, y = pos
            if kind == ">":
                forward = ((x + 1) % self.size["x"], y)

            elif kind == "v":
                forward = (x, (y + 1) % self.size["y"])

            if self[pos] == kind and self[forward] == ".":
                to_move.append((pos, forward))

        for pos, forward in to_move:
            self[pos] = "."
            self[forward] = kind

        return len(to_move)


if __name__ == "__main__":
    task_input = load_input(year=2021, day=25, group_lines=False)
    cucumbers = GameOfCucumbers(task_input)
    steps = cucumbers.run_until_stable()
    print(f"Part 1: {steps}")

    # part2 = ""
    # print(f"Part 2: {part2}")
