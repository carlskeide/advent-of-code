# coding=utf-8
import re

from ..utils import load_input
from ..models import SparseGrid


def parse_sensor(line):
    parsed = re.findall(r"x=(-?\d+), y=(-?\d+)", line)

    return {
        "sensor": (int(parsed[0][0]), int(parsed[0][1])),
        "beacon": (int(parsed[1][0]), int(parsed[1][1])),
    }


class Zone(SparseGrid):
    def __init__(self, scan):
        super().__init__()

        self.empty = []
        for item in scan:
            self.mark_sensor(**item)

    def mark_sensor(self, sensor, beacon):
        self[sensor] = "S"
        self[beacon] = "B"

        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        for x in range(sensor[0] - distance, sensor[0] + distance + 1):
            y_mod = distance - abs(sensor[0] - x)
            for y in range(sensor[1] - y_mod, sensor[1] + y_mod + 1):
                if (x, y) not in self.state:
                    self[(x, y)] = "#"


if __name__ == "__main__":
    scan = [parse_sensor(line) for line in load_input(year=2022, day=15)]
    zone = Zone(scan)

    part1 = ""
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
