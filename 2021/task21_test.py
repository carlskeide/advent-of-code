# coding=utf-8
from unittest import TestCase

from .task21 import *


class TestTask(TestCase):
    def test_part1(self):
        game = GameOfDice({1: 4, 2: 8})
        game.run_until(1000)
        self.assertEqual(game.score, {1: 1000, 2: 745})
        self.assertEqual(game.rolls, 993)

    def test_part2(self):
        pass
