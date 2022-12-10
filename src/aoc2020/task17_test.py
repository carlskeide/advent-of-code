# coding=utf-8
from unittest import TestCase

from .task17 import GameOfCubes


class TestGameOfCubes(TestCase):
    def test_step(self):
        inital = [
            ".#.",
            "..#",
            "###"
        ]

        game = GameOfCubes(inital)
        self.assertEqual(game.active, 5)

        game.step()
        self.assertEqual(game.active, 11)

        game.step()
        self.assertEqual(game.active, 21)
