# coding=utf-8
from unittest import TestCase

from .task03 import *


class TestTask(TestCase):
    sample_charter = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

    def test_priority(self):
        self.assertEqual(priority("p"), 16)
        self.assertEqual(priority("L"), 38)

    def test_part1(self):
        common = [
            find_common(line) for line in self.sample_charter
        ]
        self.assertListEqual(common, ["p", "L", "P", "v", "t", "s"])

    def test_part2(self):
        self.assertEqual(find_group(self.sample_charter[:3]), "r")
        self.assertEqual(find_group(self.sample_charter[3:]), "Z")
