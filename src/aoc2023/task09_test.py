# coding=utf-8
from unittest import TestCase

from .task09 import *


class TestTask(TestCase):
    sample_input = (
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45]
    )

    def test_part1(self):
        self.assertEqual(extrapolate(self.sample_input[0]), 18)
        self.assertEqual(extrapolate(self.sample_input[1]), 28)
        self.assertEqual(extrapolate(self.sample_input[2]), 68)

    def test_part2(self):
        self.assertEqual(extrapolate(list(reversed(self.sample_input[0]))), -3)
        self.assertEqual(extrapolate(list(reversed(self.sample_input[1]))), 0)
        self.assertEqual(extrapolate(list(reversed(self.sample_input[2]))), 5)
