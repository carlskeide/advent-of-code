# coding=utf-8
from unittest import TestCase

from .task08 import *


class TestTask(TestCase):
    heightmap = [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0]
    ]

    def test_part1(self):
        self.assertEqual(visible_trees(self.heightmap), 21)

    def test_part2(self):
        pass
