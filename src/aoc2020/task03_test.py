# coding=utf-8
from unittest import TestCase

from .task03 import toboggan


class TestTask(TestCase):
    sample_terrain = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]

    def test_toboggan(self):
        assert sum(toboggan(self.sample_terrain, delta_x=3, delta_y=1)) == 7
