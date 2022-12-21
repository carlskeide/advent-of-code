# coding=utf-8
from unittest import TestCase

from .task20 import *


class TestTask(TestCase):
    sample_input = [1, 2, -3, 3, -2, 0, 4]

    def test_part1(self):
        zero = build_list(self.sample_input, rounds=1)

        self.assertEqual(seek(zero, 1000).val, 4)
        self.assertEqual(seek(zero, 2000).val, -3)
        self.assertEqual(seek(zero, 3000).val, 2)

    def test_part2(self):
        big_numbers = (i * 811589153 for i in self.sample_input)
        zero = build_list(big_numbers, rounds=10)

        self.assertEqual(seek(zero, 1000).val, 811589153)
        self.assertEqual(seek(zero, 2000).val, 2434767459)
        self.assertEqual(seek(zero, 3000).val, -1623178306)
