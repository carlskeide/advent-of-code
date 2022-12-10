# coding=utf-8
from ..utils import load_input


def transform(subject, loop_size=1):
    num = 1
    for _ in range(loop_size):
        num *= subject
        num %= 20201227

    return num


def find_loop_size(public):
    i = 0
    num = 1
    while num != public:
        i += 1
        num *= 7
        num %= 20201227

    return i


if __name__ == "__main__":
    door_public, card_public = [int(line) for line in load_input(year=2020, day=25)]
    door_loop = find_loop_size(door_public)
    door_secret = transform(card_public, loop_size=door_loop)
    print(f"Part 1: {door_secret}")

    part2 = ""
    print(f"Part 2: {part2}")
