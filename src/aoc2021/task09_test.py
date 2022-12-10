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


class TestHeightMap(TestCase):
    def setUp(self):
        self.heightmap = HeightMap(TEST_MAP)

    def test_init(self):
        self.assertDictEqual(self.heightmap.size, {"x": 10, "y": 5})
        self.assertListEqual(
            self.heightmap.state[2],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2])

    def test_find_lows(self):
        self.assertEqual(list(self.heightmap.find_lows()), [1, 0, 5, 5])

    def test_find_basins(self):
        self.assertListEqual(
            [len(basin) for basin in self.heightmap.find_basins()],
            [3, 9, 14, 9])
