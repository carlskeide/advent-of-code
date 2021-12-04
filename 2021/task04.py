# coding=utf-8
from . import load_input

def parse_boards(charter):
    return [
        [row.split() for row in board.splitlines()]
        for board in charter
    ]


def has_bingo(board):
    cols = [[board[y][x] for y in range(5)] for x in range(5)]
    return any(all(c == "" for c in row) for row in board + cols)


def score_board(board, number):
    return [["" if c == number else c for c in row] for row in board]


def board_value(board):
    return sum(sum(int(col) for col in row if col) for row in board)


def play_bingo(boards, numbers):
    for number in numbers:
        print(f"calling number {number}")
        boards = [score_board(board, number) for board in boards]
        for board in boards:
            if has_bingo(board):
                print("BINGO")
                return board, number



if __name__ == "__main__":
    task_input = load_input(day=4, group_lines=True)
    numbers = (n for n in task_input[0].split(','))
    boards = parse_boards(task_input[1:])

    board, number = play_bingo(boards, numbers)
    part1 = board_value(board) * int(number)
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
