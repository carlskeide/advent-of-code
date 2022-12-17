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
    def __init__(self, scan, watch_row=None):
        super().__init__()

        self.empty = set()
        self.watch_row = watch_row
        for item in scan:
            self.mark_sensor(**item)

    def mark_sensor(self, sensor, beacon):
        self[sensor] = "S"
        self[beacon] = "B"

        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        print(f"sensor {sensor} beacon: {beacon}, distance: {distance}")
        for y in range(sensor[1] - distance, sensor[1] + distance + 1):
            if y == self.watch_row:
                x_mod = distance - abs(sensor[1] - y)
                for x in range(sensor[0] - x_mod, sensor[0] + x_mod + 1):
                    if (x,y) not in self.state:
                        self.empty.add((x,y))


if __name__ == "__main__":
    scan = [parse_sensor(line) for line in load_input(year=2022, day=15)]
    zone = Zone(scan, watch_row=2000000)

    part1 = len(zone.empty)
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
