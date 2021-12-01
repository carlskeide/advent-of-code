# coding=utf-8
from unittest import TestCase

from .task01 import *

class TestTask(TestCase):
    def test_part1(self):
        depths = [
            199, 200, 208, 210, 200, 207, 240, 269, 260, 263
        ]

        self.assertEqual(num_increases(depths), 7)
