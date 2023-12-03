# coding=utf-8
import string
from typing import Iterator
from ..utils import load_input
from ..models import SimpleGrid, Charter, Pos2D

SYMBOLS = set(string.punctuation) - set(".")


class Engine(SimpleGrid):
    def __init__(self, charter: Charter) -> None:
        super().__init__(charter)

        self.numbers = []
        self.gears = []

        for y, row in enumerate(self.state):
            buffer = []
            for x, val in enumerate(row):
                if val == "*":
                    self.gears.append((x, y))

                if val.isdigit():
                    buffer.append((x, y))

                elif len(buffer):
                    self.numbers.append(buffer)
                    buffer = []

            if len(buffer):
                self.numbers.append(buffer)

    def make_int(self, positions: list[Pos2D]) -> int:
        return int("".join(self[position] for position in positions))

    @property
    def part_numbers(self) -> Iterator[int]:
        for number_pos in self.numbers:
            neighbors = {
                self[neighbor]
                for pos in number_pos
                for neighbor in self.neighbors(pos, cardinal=False)
                if neighbor not in number_pos
            }
            if any(neighbor in SYMBOLS for neighbor in neighbors):
                yield self.make_int(number_pos)

    @property
    def gear_values(self) -> Iterator[int]:
        for gear in self.gears:
            neighbors = set(self.neighbors(gear, cardinal=False))
            adjacent = [
                number_pos for number_pos in self.numbers
                if any(neighbor in number_pos for neighbor in neighbors)
            ]

            if len(adjacent) == 2:
                yield self.make_int(adjacent[0]) * self.make_int(adjacent[1])


if __name__ == "__main__":
    task_input = load_input(year=2023, day=3, group_lines=False)
    engine = Engine(task_input)

    part1 = sum(engine.part_numbers)
    print(f"Part 1: {part1}")

    part2 = sum(engine.gear_values)
    print(f"Part 2: {part2}")
