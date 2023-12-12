# coding=utf-8
from unittest import TestCase

from .task11 import *


class TestTask(TestCase):
    sample_input = (
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#.....",
    )

    def test_expand(self):
        universe = Universe(self.sample_input)
        self.assertEqual(
            str(universe),
            (
                "...#......\n"
                ".......#..\n"
                "#.........\n"
                "..........\n"
                "......#...\n"
                ".#........\n"
                ".........#\n"
                "..........\n"
                ".......#..\n"
                "#...#....."
            ))
        universe.expand()
        self.assertEqual(
            str(universe),
            (
                "....#........\n"
                ".........#...\n"
                "#............\n"
                ".............\n"
                ".............\n"
                "........#....\n"
                ".#...........\n"
                "............#\n"
                ".............\n"
                ".............\n"
                ".........#...\n"
                "#....#......."
            ))

    def test_part1(self):
        universe = Universe(self.sample_input)
        universe.expand()
        self.assertEqual(sum(universe.distances()), 374)

    def test_part2(self):
        universe = Universe(self.sample_input)
        universe.expand(10)
        self.assertEqual(sum(universe.distances()), 1030)
