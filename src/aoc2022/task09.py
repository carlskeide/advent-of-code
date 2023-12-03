# coding=utf-8
from ..utils import load_input
from ..models import SparseGrid


class Rope(SparseGrid):
    moves = {
        "U": (0, -1),
        "D": (0, 1),
        "L": (-1, 0),
        "R": (1, 0),
    }

    def __init__(self, length=2):
        super().__init__()

        self.nodes = [(0, 0)] * length
        self[(0, 0)] = "s"


    def move(self, direction, distance):
        head_dx, head_dy = self.moves[direction]

        for _ in range(distance):
            head_x, head_y = self.nodes[0]
            self.nodes[0] = (head_x + head_dx, head_y + head_dy)

            for i in range(1, len(self.nodes)):
                node = self.nodes[i]
                prev_node = self.nodes[i - 1]

                if (node != prev_node
                    and node not in self.neighbors(prev_node, cardinal=False)):

                    node_x, node_y = node
                    prev_x, prev_y = prev_node

                    if prev_x != node_x:
                        node_x += 1 if prev_x > node_x else -1

                    if prev_y != node_y:
                        node_y += 1 if prev_y > node_y else -1

                    self.nodes[i] = (node_x, node_y)

            self[self.nodes[-1]] = "#"


if __name__ == "__main__":
    instructions = [
        (direction, int(distance)) for direction, distance
        in map(str.split, load_input(year=2022, day=9))
    ]

    rope = Rope(length=2)
    for direction, distance in instructions:
        rope.move(direction, distance)

    part1 = len(rope.values())
    print(f"Part 1: {part1}")

    rope = Rope(length=10)
    for direction, distance in instructions:
        rope.move(direction, distance)
    part2 = len(rope.values())
    print(f"Part 2: {part2}")
