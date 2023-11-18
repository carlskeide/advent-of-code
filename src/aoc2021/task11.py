# coding=utf-8
from ..utils import load_input
from ..models import SimpleGrid


class GameOfSquids(SimpleGrid):
    def __init__(self, charter):
        super().__init__((map(int, line) for line in charter), cardinal=False)

        self.steps = 0
        self.flashes = 0

    def step(self):
        for position in self:
            self[position] += 1

        flashed = set()
        hits = True
        while hits:
            hits = [position for position in self
                    if position not in flashed and self[position] > 9]

            for position in hits:
                flashed.add(position)
                for neighbor in self.neighbors(position):
                    self[neighbor] += 1

        self.flashes += len(flashed)
        for position in flashed:
            self[position] = 0

        self.steps += 1

    def run_until_synchronized(self):
        while sum(sum(line) for line in self.state):
            self.step()

if __name__ == "__main__":
    task_input = load_input(year=2021, day=11, group_lines=False)
    cave = GameOfSquids(task_input)
    for _ in range(100):
        cave.step()

    part1 = cave.flashes
    print(f"Part 1: {part1}")

    new_cave = GameOfSquids(task_input)
    new_cave.run_until_synchronized()
    part2 = new_cave.steps
    print(f"Part 2: {part2}")
