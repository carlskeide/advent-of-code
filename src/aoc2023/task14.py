# coding=utf-8
from ..utils import load_input
from ..models import SimpleGrid, Pos2D


class RockMap(SimpleGrid):
    def slide(self, position: Pos2D, direction: str) -> None:
        self[position] = "."
        while True:
            try:
                next_pos = self.neighbor(position, direction)

            except IndexError:
                break

            if self[next_pos] != ".":
                break

            position = next_pos

        self[position] = "O"

    def tilt(self, direction: str) -> None:
        rocks = [pos for pos in self if self[pos] == "O"]
        if direction in "se":
            rocks = reversed(rocks)

        for rock_pos in rocks:
            self.slide(rock_pos, direction)

    def spin(self, iterations):
        cache = set()
        pattern_start = None
        pattern_len = 1

        for i in range(1, iterations + 1):
            for direction in "nwse":
                self.tilt(direction)

            s = str(self)
            if s in cache:
                if pattern_start:
                    pattern_len = i - pattern_start
                    break

                else:
                    cache = set()
                    pattern_start = i

            cache.add(s)

        for _ in range((iterations - i) % pattern_len):
            for direction in "nwse":
                self.tilt(direction)

    def load(self) -> int:
        return sum(self.size["y"] - y for x, y in self if self[(x, y)] == "O")


if __name__ == "__main__":
    task_input = load_input(year=2023, day=14, group_lines=False)

    rocks = RockMap(task_input)
    rocks.tilt("n")
    part1 = rocks.load()
    print(f"Part 1: {part1}")

    rocks = RockMap(task_input)
    rocks.spin(1000000000)
    part2 = rocks.load()
    print(f"Part 2: {part2}")
