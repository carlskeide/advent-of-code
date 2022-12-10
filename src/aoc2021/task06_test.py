# coding=utf-8
from unittest import TestCase

from .task06 import *


class TestTask(TestCase):
    def test_part1(self):
        fishes = [3, 4, 3, 1, 2]
        self.assertEqual(simulate(fishes, days=18), 26)
        self.assertEqual(simulate(fishes, days=80), 5934)

    def test_part2(self):
        fishes = [3, 4, 3, 1, 2]
        self.assertEqual(simulate(fishes, days=256), 26984457539)
