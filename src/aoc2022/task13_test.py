# coding=utf-8
from unittest import TestCase

from .task13 import *


class TestTask(TestCase):
    sample_pairs = [
        ([1,1,3,1,1], [1,1,5,1,1]),
        ([[1],[2,3,4]], [[1],4]),
        ([9], [[8,7,6]]),
        ([[4,4],4,4], [[4,4],4,4,4]),
        ([7,7,7,7], [7,7,7]),
        ([], [3]),
        ([[[]]], [[]]),
        ([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9])
    ]

    def test_part1(self):
        self.assertTrue(is_sorted(*self.sample_pairs[0]))
        self.assertTrue(is_sorted(*self.sample_pairs[1]))
        self.assertFalse(is_sorted(*self.sample_pairs[2]))
        self.assertTrue(is_sorted(*self.sample_pairs[3]))
        self.assertFalse(is_sorted(*self.sample_pairs[4]))
        self.assertTrue(is_sorted(*self.sample_pairs[5]))
        self.assertFalse(is_sorted(*self.sample_pairs[6]))
        self.assertFalse(is_sorted(*self.sample_pairs[7]))

    def test_part2(self):
        pass
