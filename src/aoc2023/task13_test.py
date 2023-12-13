# coding=utf-8
from unittest import TestCase

from .task13 import *


class TestTask(TestCase):
    def test_part1(self):
        hori_map = MirrorMap((
            "#...##..#",
            "#....#..#",
            "..##..###",
            "#####.##.",
            "#####.##.",
            "..##..###",
            "#....#..#"
        ))
        self.assertEqual(hori_map.value(), 400)

        vert_map = MirrorMap((
            "#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#."
        ))
        self.assertEqual(vert_map.value(), 5)

    def test_part2(self):
        pass
