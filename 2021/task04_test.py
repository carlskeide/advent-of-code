# coding=utf-8
from unittest import TestCase

from .task04 import *

TEST_NUMBERS = list(map(int,
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,"
    "13,6,15,25,12,22,18,20,8,19,3,26,1".split(",")
))

TEST_BOARDS = [
    "22 13 17 11  0\n"
    " 8  2 23  4 24\n"
    "21  9 14 16  7\n"
    " 6 10  3 18  5\n"
    " 1 12 20 15 19\n",

    " 3 15  0  2 22\n"
    " 9 18 13 17  5\n"
    "19  8  7 25 23\n"
    "20 11 10 24  4\n"
    "14 21 16 12  6\n",

    "14 21 17 24  4\n"
    "10 16 15  9 19\n"
    "18  8 23 26 20\n"
    "22 11 13  6  5\n"
    " 2  0 12  3  7\n"
]

BINGO_BOARD = [
    [None, None, None, None, None],
    [10, 16, 15, None, 19],
    [18, 8, None, 26, 20],
    [22, None, 13, 6, None],
    [None, None, 12, 3, None]
]

LAST_BOARD = [
    [3, 15, None, None, 22],
    [None, 18, None, None, None],
    [19, 8, None, 25, None],
    [20, None, None, None, None],
    [None, None, None, 12, 6]
]


class TestBingoBoard(TestCase):
    def setUp(self):
        self.board = BingoBoard(TEST_BOARDS[0])

    def test_init(self):
        self.assertListEqual(
            self.board.rows,
            [
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19]
            ]
        )

    def test_has_bingo(self):
        self.assertFalse(self.board.bingo)

        self.board.rows = BINGO_BOARD
        self.assertTrue(self.board.bingo)

        self.board.rows = LAST_BOARD
        self.assertTrue(self.board.bingo)

    def test_call(self):
        self.board.call(18)
        self.board.call(2)
        self.board.call(25)

        self.assertListEqual(
            self.board.rows,
            [
                [22, 13, 17, 11, 0],
                [8, None, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, None, 5],
                [1, 12, 20, 15, 19]
            ]
        )

    def test_value(self):
        self.board.rows = BINGO_BOARD
        self.assertEqual(self.board.value, 188)

        self.board.rows = LAST_BOARD
        self.assertEqual(self.board.value, 148)


class TestTask(TestCase):
    def setUp(self):
        self.boards = list(map(BingoBoard, TEST_BOARDS))

    def test_part1(self):
        board, number = play_bingo(self.boards, TEST_NUMBERS)

        self.assertEqual(number, 24)
        self.assertEqual(board.rows, BINGO_BOARD)


    def test_part2(self):
        board, number = play_bingo(self.boards, TEST_NUMBERS, win=False)

        self.assertEqual(number, 13)
        self.assertEqual(board.rows, LAST_BOARD)
