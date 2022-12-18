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


class AirDrop(SparseCube):
    def __init__(self, coordinates):
        super().__init__(coordinates)

        scan_min, scan_max = self.size
        min_border = tuple(i - 1 for i in scan_min)
        max_border = tuple(i + 1 for i in scan_max)

        self.air = set()
        to_scan = [min_border, ]
        while to_scan:
            point = to_scan.pop()
            self.air.add(point)
            for neighbor in self.neighbors(point):
                if (
                    neighbor not in self.state
                    and neighbor not in self.air
                    and min(neighbor) >= min(min_border)
                    and max(neighbor) <= max(max_border)
                ):
                    to_scan.append(neighbor)

        for point in self.air:
            for neighbor in self.neighbors(point):
                if neighbor in self.state:
                    self[neighbor] += 1


if __name__ == "__main__":
    coordinates = {
        tuple(int(atom) for atom in line.split(",")): 0
        for line in load_input(year=2022, day=18)
    }

    part1 = LavaDrop(coordinates.copy())
    print(f"Part 1: {sum(part1.values())}")

    part2 = AirDrop(coordinates.copy())
    print(f"Part 2: {sum(part2.values())}")
