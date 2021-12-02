# coding=utf-8
from . import load_input

class Submarine(object):
    def __init__(self):
        super(Submarine, self).__init__()
        self.distance = 0
        self.depth = 0

    def run(self, instructions):
        for instruction in instructions:
            command, value = instruction.split()

            if command == "forward":
                self.distance += int(value)

            elif command == "down":
                self.depth += int(value)

            elif command == "up":
                self.depth -= int(value)


if __name__ == "__main__":
    instructions = load_input(day=2, group_lines=False)

    submarine = Submarine()
    submarine.run(instructions)

    part1 = submarine.distance * submarine.depth
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
