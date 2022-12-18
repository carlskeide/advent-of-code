# coding=utf-8
from ..utils import load_input
from ..models import SparseCube


class LavaDrop(SparseCube):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        for point in self:
            connected_points = sum(
                (neighbor in self.state)
                for neighbor in self.neighbors(point)
            )
            self[point] = 6 - connected_points

if __name__ == "__main__":
    coordinates = {
        tuple(int(atom) for atom in line.split(",")): 0
        for line in load_input(year=2022, day=18)
    }

    part1 = LavaDrop(coordinates)
    print(f"Part 1: {sum(part1.values())}")

    part2 = ""
    print(f"Part 2: {part2}")
