# coding=utf-8
from itertools import cycle
from .utils import load_input


class GameOfDice:
    def __init__(self, players):
        self.players = players
        self.score = {player: 0 for player in players}

        self.dice = cycle(range(1, 100 + 1))
        self.rolls = 0

    def run_until(self, target):
        turn_order = cycle(sorted(self.players))
        while max(self.score.values()) < target:
            player = next(turn_order)
            move = sum(next(self.dice) for _ in range(3))
            self.rolls += 3

            position = (self.players[player] + move) % 10 or 10
            self.players[player] = position
            self.score[player] += position


if __name__ == "__main__":
    task_input = load_input(day=21, group_lines=False)
    players = {
        int(word[1]): int(word[4]) for word in map(str.split, task_input)
    }

    game = GameOfDice(players)
    game.run_until(1000)
    print(f"Part 1: {min(game.score.values()) * game.rolls}")

    # part2 = ""
    # print(f"Part 2: {part2}")
