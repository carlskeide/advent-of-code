# coding=utf-8
from unittest import TestCase

from .task03 import get_gamma, to_epsilon, filter_common


class TestTask(TestCase):
    codes = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
    ]

    def test_part1(self):
        gamma = get_gamma(self.codes)
        self.assertEqual(gamma, "10110")
        self.assertEqual(int(gamma, 2), 22)

        epsilon = to_epsilon(gamma)
        self.assertEqual(epsilon, "01001")
        self.assertEqual(int(epsilon, 2), 9)

    def test_filter_common(self):
        self.assertEqual(filter_common(self.codes), "10111")
        self.assertEqual(filter_common(self.codes, invert=True), "01010")
