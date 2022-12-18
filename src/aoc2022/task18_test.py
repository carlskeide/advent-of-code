# coding=utf-8
from unittest import TestCase

from .task18 import *


class TestTask(TestCase):
    sample_input = {
        (2,2,2): 0,
        (1,2,2): 0,
        (3,2,2): 0,
        (2,1,2): 0,
        (2,3,2): 0,
        (2,2,1): 0,
        (2,2,3): 0,
        (2,2,4): 0,
        (2,2,6): 0,
        (1,2,5): 0,
        (3,2,5): 0,
        (2,1,5): 0,
        (2,3,5): 0
    }

    def test_part1(self):
        drop = LavaDrop(self.sample_input)
        self.assertEqual(sum(drop.values()), 64)

    def test_part2(self):
        pass
