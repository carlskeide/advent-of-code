# coding=utf-8
from enum import Enum

from ..utils import load_input


class Shapes(Enum):
    ROCK = A = X = 0
    PAPER = B = Y = 1
    SCISSORS = C = Z = 2


def basic_game(challenge, response):
    their_move, my_move = Shapes[challenge], Shapes[response]

    if their_move == my_move:
        score =  3

    elif their_move.value == (my_move.value + 1) % 3:
        score =  0

    else:
        score =  6

    return score + my_move.value + 1


def advanced_game(challenge, outcome):
    their_move = Shapes[challenge]
    if outcome == "X":
        return ((their_move.value + 2) % 3) + 1

    elif outcome == "Y":
        return their_move.value + 4

    else:
        return ((their_move.value + 1) % 3) + 7


if __name__ == "__main__":
    strategy = [
        line.split() for line
        in load_input(year=2022, day=2, group_lines=False)
    ]

    part1 = [basic_game(*moves) for moves in strategy]
    print(f"Part 1: {sum(part1)}")

    part2 = [advanced_game(*moves) for moves in strategy]
    print(f"Part 2: {sum(part2)}")
