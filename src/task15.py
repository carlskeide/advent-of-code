# coding=utf-8
from . import load_input


def memory_game(seed, limit=10):
    memory = []
    for i in range(limit):
        if i < len(seed):
            number = seed[i]

        else:
            for j, n in enumerate(reversed(memory)):
                if j == 0:
                    last_num = n

                elif n == last_num:
                    number = j
                    break

            else:
                number = 0

        memory.append(number)

    return memory


if __name__ == "__main__":
    task_input = load_input(day=15)
    seed = [int(n) for n in task_input[0].split(",")]

    memory = memory_game(seed, limit=2020)
    print(f"Part 1: {memory[-1]}")

    memory = memory_game(seed, limit=30000000)
    print(f"Part 2: {memory[-1]}")
