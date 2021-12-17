# coding=utf-8
from unittest import TestCase

from .task15 import *

TEST_CAVE = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581"
]


class TestTask(TestCase):
    def test_part1(self):
        cave = DangerCave(TEST_CAVE)
        cave.assign_costs()
        self.assertEqual(cave[-1,-1], 40)
