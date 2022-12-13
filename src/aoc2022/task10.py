# coding=utf-8
from ..utils import load_input


class Adder:
    def __init__(self, instructions):
        self.instructions = list(reversed(instructions))

        self.state = 1
        self.cycle = 1
        self.stack = None

    def run_to(self, stop, output=False):
        while self.cycle < stop:
            if output:
                print(
                    "#" if self.cycle % 40 - 1 in (
                        self.state, self.state - 1, self.state + 1
                    ) else ".", end=""
                )

            if self.stack:
                self.state += self.stack
                self.stack = None

            else:
                instruction = self.instructions.pop()
                if instruction.startswith("addx"):
                    self.stack = int(instruction.split()[-1])

            self.cycle += 1


if __name__ == "__main__":
    task_input = load_input(year=2022, day=10, group_lines=False)

    program = Adder(task_input)

    signal_strengths = []
    for cycle in (20, 60, 100, 140, 180, 220):
        program.run_to(cycle)
        signal_strengths.append(cycle * program.state)

    print(f"Part 1: {sum(signal_strengths)}")

    program = Adder(task_input)
    print(f"Part 2:")

    print(".", end="")  # ¯\_(ツ)_/¯
    for cycle in (40, 80, 120, 160, 200, 240):
        program.run_to(cycle, output=True)
        print("")
