# coding=utf-8
from unittest import TestCase

from .task09 import *

TEST_MAP = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678"
]


class TestTask(TestCase):
    def test_make_map(self):
        heightmap = make_map(TEST_MAP)
        self.assertEqual(len(heightmap), 5)
        self.assertListEqual(heightmap[2], [9, 8, 5, 6, 7, 8, 9, 8, 9, 2])

    def test_part1(self):
        heightmap = make_map(TEST_MAP)
        self.assertEqual(list(find_lows(heightmap)), [1, 0, 5, 5])

    def test_part2(self):
        pass
