# coding=utf-8
from unittest import TestCase

from .task04 import *

TEST_NUMBERS = (
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,"
    "6,15,25,12,22,18,20,8,19,3,26,1".split(",")
)

TEST_BOARDS = [
    [
        ['22', '13', '17', '11', '0'],
        ['8', '2', '23', '4', '24'],
        ['21', '9', '14', '16', '7'],
        ['6', '10', '3', '18', '5'],
        ['1', '12', '20', '15', '19']
    ],
    [
        ['3', '15', '0', '2', '22'],
        ['9', '18', '13', '17', '5'],
        ['19', '8', '7', '25', '23'],
        ['20', '11', '10', '24', '4'],
        ['14', '21', '16', '12', '6']
    ],
    [
        ['14', '21', '17', '24', '4'],
        ['10', '16', '15', '9', '19'],
        ['18', '8', '23', '26', '20'],
        ['22', '11', '13', '6', '5'],
        ['2', '0', '12', '3', '7']
    ]
]

BINGO_BOARD = [
    ['', '', '', '', ''],
    ['10', '16', '15', '', '19'],
    ['18', '8', '', '26', '20'],
    ['22', '', '13', '6', ''],
    ['', '', '12', '3', '']
]

LAST_BOARD = [
    ['3', '15', '', '', '22'],
    ['', '18', '', '', ''],
    ['19', '8', '', '25', ''],
    ['20', '', '', '', ''],
    ['', '', '', '12', '6']
]


class TestTask(TestCase):
    def test_parse_boards(self):
        board_input = [
            "22 13 17 11  0\n"
            " 8  2 23  4 24\n"
            "21  9 14 16  7\n"
            " 6 10  3 18  5\n"
            " 1 12 20 15 19\n"
        ]

        self.assertListEqual(
            parse_boards(board_input)[0][0],
            ["22", "13", "17", "11", "0"]
        )

    def test_has_bingo(self):
        self.assertFalse(has_bingo(TEST_BOARDS[0]))
        self.assertTrue(has_bingo(BINGO_BOARD))
        self.assertTrue(has_bingo(
            [['14', '21', '17', '24', ''],
            ['10', '16', '15', '', ''],
            ['18', '8', '', '26', ''],
            ['22', '', '13', '6', ''],
            ['', '', '12', '3', '']]
        ))

    def test_score_board(self):
        self.assertEqual(
            score_board(
                [['14', '21', '17', '24', '4'],
                ['10', '16', '15', '9', '19'],
                ['18', '8', '23', '26', '20'],
                ['22', '11', '13', '6', '5'],
                ['2', '0', '12', '3', '7']],
                '18'
            ),
            [['14', '21', '17', '24', '4'],
            ['10', '16', '15', '9', '19'],
            ['', '8', '23', '26', '20'],
            ['22', '11', '13', '6', '5'],
            ['2', '0', '12', '3', '7']],
        )

    def test_board_value(self):
        self.assertEqual(board_value(BINGO_BOARD), 188)
        self.assertEqual(board_value(LAST_BOARD), 148)

    def test_part1(self):
        board, number = play_bingo(TEST_BOARDS, TEST_NUMBERS)
        self.assertEqual(board, BINGO_BOARD)
        self.assertEqual(number, "24")


    def test_part2(self):
        board, number = play_bingo(TEST_BOARDS, TEST_NUMBERS, win=False)
        self.assertEqual(number, "13")
        self.assertEqual(board, LAST_BOARD)
