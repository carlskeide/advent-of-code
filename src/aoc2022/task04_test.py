# coding=utf-8
from unittest import TestCase

from .task04 import *


class TestTask(TestCase):
    sample_assignments = [
        ("2-4", "6-8"),
        ("2-3", "4-5"),
        ("5-7", "7-9"),
        ("2-8", "3-7"),
        ("6-6", "4-6"),
        ("2-6", "4-8")
    ]

    def test_part1(self):
        self.assertFalse(is_redundant(self.sample_assignments[0]))
        self.assertTrue(is_redundant(self.sample_assignments[3]))
        self.assertTrue(is_redundant(self.sample_assignments[4]))

    def test_part2(self):
        pass
