# coding=utf-8
from unittest import TestCase
from functools import partial

from .task01 import *


class TestTask(TestCase):

    sample_input = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet"
    ]

    textual_input = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ]

    def test_part1(self):
        self.assertEqual(
            (12, 38, 15, 77),
            tuple(map(
                calibration_value, self.sample_input))
        )

    def test_part2(self):
        self.assertEqual(
            (29, 83, 13, 24, 42, 14, 76),
            tuple(map(
                partial(calibration_value, textual=True), self.textual_input))
        )
