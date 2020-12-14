# coding=utf-8
from . import load_input

import re


def parse_program(input_data):
    mask = input_data[0].split(" = ")[1]
    program = []

    for line in input_data[1:]:
        addr, value = re.match(r"^mem\[(\d+)\] = (\d+)$", line).groups()
        program.append((int(addr), int(value)))

    return mask, program


def masked_value(mask, value):
    bin_value = f"{value:036b}"

    masked = ""
    for bit, mask_bit in zip(bin_value, mask):
        masked += bit if mask_bit == "X" else mask_bit

    return int(masked, 2)


def run_program(programs):
    memory = {}

    for program in programs:
        mask, instructions = parse_program(program)
        for addr, value in instructions:
            memory[addr] = masked_value(mask, value)

    return memory


if __name__ == "__main__":
    task_input = load_input(day=14)

    programs = []
    for line in task_input:
        if line.startswith("mask"):
            program = []
            programs.append(program)

        program.append(line)

    memory = run_program(programs)
    print(f"Part 1: {sum(memory.values())}")

    part2 = ""
    print(f"Part 2: {part2}")
