# coding=utf-8
from unittest import TestCase

from .task17 import *


class TestTask(TestCase):
    sample_input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

    def test_part1(self):
        game = Tetris(self.sample_input)
        for _ in range(2022):
            game.play()

        self.assertEqual(game.height, 3068)

    def test_part2(self):
        pass
