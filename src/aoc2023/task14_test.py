# coding=utf-8
from unittest import TestCase

from .task14 import *


class TestTask(TestCase):
    sample_input = (
        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#....",
    )

    def test_part1(self):
        rocks = RockMap(self.sample_input)
        rocks.tilt("n")
        self.assertEqual(rocks.load(), 136)

    def test_part2(self):
        rocks = RockMap(self.sample_input)
        rocks.spin(1000000000)
        self.assertEqual(rocks.load(), 64)
