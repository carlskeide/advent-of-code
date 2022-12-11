# coding=utf-8
from unittest import TestCase

from .task02 import *


class TestTask(TestCase):
    strategy = [
        ("A", "Y"),
        ("B", "X"),
        ("C", "Z")
    ]

    def test_part1(self):
        self.assertListEqual(
            [basic_game(*moves) for moves in self.strategy],
            [8, 1, 6]
        )

    def test_part2(self):
        self.assertListEqual(
            [advanced_game(*moves) for moves in self.strategy],
            [4, 1, 7]
        )
