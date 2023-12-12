# coding=utf-8
from typing import Iterator
from ..utils import load_input
from ..models import SimpleGrid, Pos2D

class PipeMap(SimpleGrid):
    directions = {
        "n": (0, -1),
        "s": (0, 1),
        "e": (1, 0),
        "w": (-1, 0)
    }

    anti_dir = {
        "n": "s",
        "s": "n",
        "e": "w",
        "w": "e"
    }

    tiles = {
        ".": "",
        "|": "ns",
        "-": "ew",
        "L": "ne",
        "J": "nw",
        "7": "sw",
        "F": "se",
        "S": "nsew"
    }

    def loop_len(self) -> int:
        start_pos = self.index("S")
        direction = next(self.connections(start_pos))
        position = self.step(start_pos, direction)
        steps = 1
        while position != start_pos:
            steps += 1
            tile = self[position]
            direction = next(d for d in self.tiles[tile]
                             if d != self.anti_dir[direction])
            position = self.step(position, direction)

        return steps

    def step(self, position: Pos2D, direction: str) -> Pos2D:
        pos_x, pos_y = position
        delta_x, delta_y = self.directions[direction]
        return (pos_x + delta_x, pos_y + delta_y)

    def connections(self, position: Pos2D) -> Iterator[str]:
        pos_x, pos_y = position
        for direction, (delta_x, delta_y) in self.directions.items():
            other_tile = self[(pos_x + delta_x, pos_y + delta_y)]
            if self.anti_dir[direction] in self.tiles[other_tile]:
                yield direction


if __name__ == "__main__":
    task_input = load_input(year=2023, day=10, group_lines=False)
    pipemap = PipeMap(task_input)
    print(pipemap)

    part1 = pipemap.loop_len() // 2
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
