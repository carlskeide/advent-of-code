# coding=utf-8
from . import load_input
from functools import reduce
from operator import mul


class HeightMap:
    def __init__(self, charter):
        self.map = [list(map(int, s)) for s in charter]

        self.size = {
            "x": len(self.map[0]),
            "y": len(self.map)
        }

    def __iter__(self):
        for y in range(self.size["y"]):
            for x in range(self.size["x"]):
                yield (x, y)

    def __getitem__(self, position):
        x, y = position
        return self.map[y][x]

    def neighbors(self, position):
        x, y = position
        for xx, yy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if (0 <= xx < self.size["x"] and 0 <= yy < self.size["y"]):
                yield (xx, yy)

    def find_lows(self):
        for position in self:
            point = self[position]
            for neighbor in self.neighbors(position):
                if point >= self[neighbor]:
                    break

            else:
                yield point

    def find_basins(self):
        explored = set()
        for position in self:
            if position in explored or self[position] == 9:
                continue

            yield self.map_basin(position, explored)
            explored.add(position)

    def map_basin(self, position, explored):
        basin = {position}
        for neighbor in self.neighbors(position):
            if neighbor not in explored:
                explored.add(neighbor)
                if self[neighbor] != 9:
                    basin.update(self.map_basin(neighbor, explored))

        return basin


if __name__ == "__main__":
    task_input = load_input(day=9, group_lines=False)
    area = HeightMap(task_input)

    lows = list(area.find_lows())
    part1 = sum(lows) + len(lows)
    print(f"Part 1: {part1}")

    basins = list(area.find_basins())
    top3 = list(sorted((len(b) for b in basins), reverse=True))[:3]
    part2 = reduce(mul, top3)
    print(f"Part 2: {part2}")
