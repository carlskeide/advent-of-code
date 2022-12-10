# coding=utf-8
from unittest import TestCase

from .task05 import *


TEST_INPUT = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


class TestTask(TestCase):
    def test_make_straight_lines(self):
        lines = list(make_lines(TEST_INPUT[:4], diagonals=False))
        self.assertEqual(len(lines), 3)
        self.assertEqual(tuple(lines[0]),
            ('0,9', '1,9', '2,9', '3,9', '4,9', '5,9'))
        self.assertEqual(tuple(lines[1]),
            ('9,4', '8,4', '7,4', '6,4', '5,4', '4,4', '3,4'))
        self.assertEqual(tuple(lines[2]),
            ("2,2", "2,1"))

    def test_make_all_lines(self):
        lines = list(make_lines(TEST_INPUT[:4], diagonals=True))
        self.assertEqual(len(lines), 4)
        self.assertEqual(tuple(lines[1]),
            ('8,0', '7,1', '6,2', '5,3', '4,4', '3,5', '2,6', '1,7', '0,8'))

    def test_part1(self):
        lines = make_lines(TEST_INPUT)
        self.assertEqual(overlap(lines), 5)

    def test_part2(self):
        lines = make_lines(TEST_INPUT, diagonals=True)
        self.assertEqual(overlap(lines), 12)
