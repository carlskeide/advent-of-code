# coding=utf-8
from ..utils import load_input

import re
from itertools import product


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


def masked_addr(mask, addr):
    bin_addr = f"{addr:036b}"
    num_wild = mask.count("X")

    masked = ""
    for bit, mask_bit in zip(bin_addr, mask):
        masked += bit if mask_bit == "0" else mask_bit

    addr_tpl = masked.replace("X", "{}")

    masked_addrs = []
    for replacements in product("01", repeat=num_wild):
        replaced = addr_tpl.format(*replacements)
        masked_addrs.append(int(replaced, 2))

    return masked_addrs


if __name__ == "__main__":
    task_input = load_input(year=2020, day=14)

    programs = []
    for line in task_input:
        if line.startswith("mask"):
            program = []
            programs.append(program)

        program.append(line)

    memory = {}
    for program in programs:
        mask, instructions = parse_program(program)
        for addr, value in instructions:
            memory[addr] = masked_value(mask, value)

    print(f"Part 1: {sum(memory.values())}")

    memory = {}
    for program in programs:
        mask, instructions = parse_program(program)
        for addr, value in instructions:
            for new_addr in masked_addr(mask, addr):
                memory[new_addr] = value

    print(f"Part 2: {sum(memory.values())}")
