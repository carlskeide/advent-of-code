# coding=utf-8
from . import load_input


class GameOfSquids(object):
    def __init__(self, charter):
        self.state = [[int(c) for c in line] for line in charter]
        self.size = len(self.state)
        self.flashes = 0

    def __iter__(self):
        for y in range(self.size):
            for x in range(self.size):
                yield (x, y)

    def __getitem__(self, position):
        x, y = position
        return self.state[y][x]

    def __setitem__(self, position, value):
        x, y = position
        self.state[y][x] = value

    def neighbors(self, position):
        x, y = position
        for xx, yy in (
            (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y), (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
        ):
            if (0 <= xx < self.size and 0 <= yy < self.size):
                yield (xx, yy)

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


if __name__ == "__main__":
    task_input = load_input(day=11, group_lines=False)
    cave = GameOfSquids(task_input)
    for _ in range(100):
        cave.step()

    part1 = cave.flashes
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
