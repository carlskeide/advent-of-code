# coding=utf-8
from . import load_input

from typing import Iterable, Tuple


class InstructionError(Exception):
    pass


class OOBError(Exception):
    pass


class InfiniteLoopError(Exception):
    pass


class GameConsole:
    def __init__(self, program: Iterable[Tuple[str, int]]) -> None:
        self.accumulator = 0
        self.index = 0
        self.cache = []
        self.program = [
            (cmd, int(arg)) for cmd, arg in map(str.split, program)
        ]

    def run(self) -> int:
        """
        The boot code is represented as a text file with one instruction per
        line of text. Each instruction consists of an operation
        (acc, jmp, or nop) and an argument (a signed number like +4 or -20).
        """
        while self.index != len(self.program):
            self._circuit_breaker()
            cmd, arg = self.program[self.index]
            self._execute(cmd, arg)

        return self.accumulator

    def _circuit_breaker(self) -> None:
        if not 0 <= self.index <= len(self.program):
            raise OOBError(self.index, len(self.program))

        elif self.index in self.cache:
            raise InfiniteLoopError(self.index, self.accumulator)

        else:
            self.cache.append(self.index)

    def _execute(self, cmd: str, arg: int) -> None:
        """
        acc increases or decreases a single global value called the accumulator by
        the value given in the argument. For example, acc +7 would increase the
        accumulator by 7. The accumulator starts at 0. After an acc instruction,
        the instruction immediately below it is executed next.
        jmp jumps to a new instruction relative to itself. The next instruction to
        execute is found using the argument as an offset from the jmp instruction;
        for example, jmp +2 would skip the next instruction, jmp +1 would continue
        to the instruction immediately below it, and jmp -20 would cause the
        instruction 20 lines above to be executed next.
        nop stands for No OPeration - it does nothing. The instruction immediately
        below it is executed next.
        """

        # print(f"{self.index}: {cmd} {arg}")

        if cmd == "acc":
            self.accumulator += arg
            self.index += 1

        elif cmd == "jmp":
            self.index += arg

        elif cmd == "nop":
            self.index += 1

        else:
            raise InstructionError(cmd)


if __name__ == "__main__":
    program = load_input(day=8)
    console = GameConsole(program)
    try:
        console.run()

    except InfiniteLoopError as e:
        print(f"Caught {e!r}")

    print(f"Part 1: {console.accumulator}")

    for i, line in enumerate(program):
        dbg_program = program.copy()

        if line.startswith("jmp"):
            dbg_program[i] = line.replace("jmp", "nop")

        elif line.startswith("nop"):
            dbg_program[i] = line.replace("nop", "jmp")

        else:
            continue

        console = GameConsole(dbg_program)
        try:
            console.run()
            break

        except InfiniteLoopError:
            continue

    print(f"Part 2: {console.accumulator}")
