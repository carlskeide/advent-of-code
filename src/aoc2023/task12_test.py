# coding=utf-8
from unittest import TestCase

from .task12 import *


class TestTask(TestCase):
    def test_part1(self):
        self.assertEqual(
            valid_combinations("?###????????", [3, 2, 1]),
            10)

    def test_part2(self):
        self.assertEqual(
            valid_combinations(*make_hard("???.###", [1,1,3])),
            1)

        # self.assertEqual(
        #     valid_combinations(*make_hard("????.######..#####.", [1,6,5])),
        #     2500)

