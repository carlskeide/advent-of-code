# coding=utf-8
from unittest import TestCase

from .task03 import *


class TestTask(TestCase):
    sample_input = (
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    )

    def test_part1(self):
        self.assertEqual(4361, sum(Engine(self.sample_input).part_numbers))

    def test_part2(self):
        self.assertEqual([16345, 451490], list(Engine(self.sample_input).gear_values))
