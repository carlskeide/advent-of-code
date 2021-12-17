# coding=utf-8
import re
from .utils import load_input
# from .models import SparseGrid


def parse_target(description):
    matched = re.match(r"^.*x=(\d+)..(\d+), y=(\-?\d+)..(\-?\d+)", description)
    x_min, x_max, y_max, y_min = map(int, matched.groups())
    return ((x_min, y_min), (x_max, y_max))


class BallisticGrid(object):
    def __init__(self, target):
        super().__init__()

        self.origin = (0, 0)
        self[0, 0] = "S"

        self.target = target
        for target_position in self[target[0]:target[1]]:
            self[target_position] = "T"

    def __str__(self):
        return "\n".join(
            "".join(
                self.get((x, y), ".")
                for x in range(self.size["x"] + 1)
            ) for y in range(self.size["y"] + 1)
        )

    @property
    def size(self):
        return {
            "x": max(x for x, y in self),
            "y": max(y for x, y in self)
        }


if __name__ == "__main__":
    task_input = load_input(day=17, group_lines=False)

    part1 = ""
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
