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
    def test_make_line(self):
        self.assertEqual(tuple(make_line("1,1 -> 1,3")),("1,1", "1,2", "1,3"))
        self.assertEqual(tuple(make_line("2,2 -> 4,2")),("2,2", "3,2", "4,2"))
        self.assertEqual(tuple(make_line("2,2 -> 2,2")),("2,2", ))
        self.assertEqual(make_line("8,0 -> 0,8"), None)

    def test_part1(self):
        lines = filter(None, map(make_line, TEST_INPUT))
        self.assertEqual(overlap(lines), 5)

    def test_part2(self):
        pass
