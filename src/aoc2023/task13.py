# coding=utf-8
from ..utils import load_input
from ..models import SimpleGrid


class MirrorMap(SimpleGrid):
    def value(self):
        for y in range(1, self.size["y"]):
            window = min(y, self.size["y"] - y)
            if self.state[y - 1::-1][:window] == self.state[y:][:window]:
                return y * 100

        cols = [
            [self.state[y][x] for y in range(self.size["y"])]
            for x in range(self.size["x"])
        ]
        for x in range(1, self.size["x"]):
            window = min(x, self.size["x"] - x)
            if cols[x - 1::-1][:window] == cols[x:][:window]:
                return x

        raise ValueError("No mirror found!")

if __name__ == "__main__":
    task_input = load_input(year=2023, day=13, group_lines=True)
    maps = [
        MirrorMap(group.splitlines()) for group in task_input
    ]

    part1 = sum(mmap.value() for mmap in maps)
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
