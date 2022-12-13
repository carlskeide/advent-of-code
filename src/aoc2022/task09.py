# coding=utf-8
from ..utils import load_input
from ..models import SparseGrid, DiagonalMixin


class Rope(DiagonalMixin, SparseGrid):
    moves = {
        "U": (0, -1),
        "D": (0, 1),
        "L": (-1, 0),
        "R": (1, 0),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.head = self.tail = (0, 0)
        self[(0, 0)] = "s"


    def move(self, direction, distance):
        head_dx, head_dy = self.moves[direction]

        for _ in range(distance):
            head_x, head_y = self.head
            self.head = (head_x + head_dx, head_y + head_dy)

            if (self.tail != self.head
                and self.tail not in self.neighbors(self.head)):

                tail_x, tail_y = self.tail
                if self.head[0] != self.tail[0]:
                    tail_x += 1 if self.head[0] > self.tail[0] else -1

                if self.head[1] != self.tail[1]:
                    tail_y += 1 if self.head[1] > self.tail[1] else -1

                self.tail = (tail_x, tail_y)

            self[self.tail] = "#"



if __name__ == "__main__":
    instruction = (
        (direction, int(distance)) for direction, distance
        in map(str.split, load_input(year=2022, day=9))
    )

    rope = Rope()
    for direction, distance in instruction:
        rope.move(direction, distance)

    part1 = len(rope.values())
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
