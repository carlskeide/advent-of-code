# coding=utf-8
from unittest import TestCase

from .task13 import *

TEST_DOTS = [
    "6,10", "0,14", "9,10", "0,3", "10,4",
    "4,11", "6,0", "6,12", "4,1", "0,13",
    "10,12", "3,4", "3,0", "8,4", "1,10",
    "2,14", "8,10", "9,0"
]


class TestTask(TestCase):
    def test_part1(self):
        paper = FoldableGrid(TEST_DOTS)
        self.assertEqual(len(paper.values()), 18)

        paper.fold("y=7")
        self.assertEqual(len(paper.values()), 17)

        paper.fold("x=5")
        self.assertEqual(len(paper.values()), 16)

    def test_part2(self):
        pass
