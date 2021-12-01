# coding=utf-8
from unittest import TestCase

from .task01 import *

class TestTask(TestCase):
    depths = [
        199, 200, 208, 210, 200, 207, 240, 269, 260, 263
    ]

    def test_part1(self):
        self.assertEqual(num_increases(self.depths), 7)

    def test_part2(self):
        self.assertEqual(sliding_increases(self.depths), 5)
