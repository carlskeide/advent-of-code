# coding=utf-8
from unittest import TestCase

from .task06 import *


class TestTask(TestCase):
    def test_part1(self):
        fishes = [3, 4, 3, 1, 2]

        self.assertListEqual(simulate(fishes, days=10),
                             [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 7, 8])

        self.assertListEqual(simulate(fishes, days=18),
                             [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2,
                              2, 3, 3, 4, 6, 7, 8, 8, 8, 8])

        self.assertEqual(len(simulate(fishes, days=80)), 5934)

    # def test_part2(self):
    #     fishes = [3, 4, 3, 1, 2]
    #     self.assertEqual(len(simulate(fishes, days=256)), 26984457539)
