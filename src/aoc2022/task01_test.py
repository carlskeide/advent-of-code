# coding=utf-8
from unittest import TestCase

from .task01 import *


class TestTask(TestCase):
    calories = [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000]
    ]

    def test_part1(self):
        result = sum(most_calories(self.calories, num=1))
        self.assertEqual(result, 24000)

    def test_part2(self):
        result = sum(most_calories(self.calories, num=3))
        self.assertEqual(result, 45000)
