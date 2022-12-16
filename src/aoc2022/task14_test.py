# coding=utf-8
from unittest import TestCase

from .task14 import *


class TestTask(TestCase):

    sample_paths = [
        [(498, 4), (498, 6), (496, 6)],
        [(503, 4), (502, 4), (502, 9), (494, 9)]
    ]

    def test_parse_cave(self):
        cave = Cave(self.sample_paths)
        self.assertEqual(
            str(cave).splitlines(),
            [
                "......+...",
                "..........",
                "..........",
                "..........",
                "....#...##",
                "....#...#.",
                "..###...#.",
                "........#.",
                "........#.",
                "#########."
            ]
        )

    def test_part1(self):
        cave = Cave(self.sample_paths)
        self.assertEqual(cave.run_until_stable(), 24)

    def test_part2(self):
        cave = FlooredCave(self.sample_paths)
        self.assertEqual(cave.run_until_stable(), 93)
