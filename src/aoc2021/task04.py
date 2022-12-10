# coding=utf-8
from ..utils import load_input


class BingoBoard():
    def __init__(self, board, size=5):
        self.size = size
        self.rows = [
            [int(col) for col in row.split()]
            for row in board.splitlines()
        ]

    @property
    def cols(self):
        return [
            [self.rows[y][x] for y in range(self.size)]
            for x in range(self.size)
        ]

    @property
    def bingo(self):
        return any(
            all(c is None for c in line)
            for line in self.rows + self.cols
        )

    @property
    def value(self):
        return sum(
            sum(filter(None, row))
            for row in self.rows
        )

    def call(self, number):
        for row in self.rows:
            if number in row:
                row[row.index(number)] = None



def play_bingo(boards, numbers, win=True):
    for number in numbers:
        print(f"calling number {number}")

        boards = [board for board in boards if not board.bingo]
        for board in boards:
            board.call(number)
            if board.bingo:
                print(f"BINGO!")

                if win or len(boards) == 1:
                    return board, number


if __name__ == "__main__":
    task_input = load_input(year=2021, day=4, group_lines=True)
    numbers = list(map(int, task_input[0].split(',')))

    boards = list(map(BingoBoard, task_input[1:]))
    board, number = play_bingo(boards, numbers)
    part1 = board.value * number
    print(f"Part 1: {part1}")

    board, number = play_bingo(boards, numbers, win=False)
    part2 = board.value * number
    print(f"Part 2: {part2}")
