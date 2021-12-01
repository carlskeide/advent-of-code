# coding=utf-8
from . import load_input

from itertools import islice


def memory_game(seed):
    last_number = number = None
    last_turn = turn = 0
    memory = {}
    while True:
        if turn < len(seed):
            number = seed[turn]

        elif last_number in memory:
            number = last_turn - memory[last_number]

        else:
            number = 0

        yield number

        memory[last_number] = last_turn
        last_turn = turn
        last_number = number
        turn += 1


if __name__ == "__main__":
    task_input = load_input(day=15)
    seed = [int(n) for n in task_input[0].split(",")]

    for number in islice(memory_game(seed), 2020):
        pass

    print(f"Part 1: {number}")

    for number in islice(memory_game(seed), 30000000):
        pass

    print(f"Part 2: {number}")
