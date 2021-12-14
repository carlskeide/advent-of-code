# coding=utf-8
from unittest import TestCase

from .task14 import *

TEST_RULES = [
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C"
]


class TestTask(TestCase):
    def test_part1(self):
        polymer = Polymer("NNCB", TEST_RULES)
        polymer.step()
        self.assertEqual(str(polymer), "NCNBCHB")
        polymer.step()
        self.assertEqual(str(polymer), "NBCCNBBBCBHCB")
        polymer.step()
        self.assertEqual(str(polymer), "NBBBCNCCNBBNBNBBCHBHHBCHB")
        polymer.step()
        self.assertEqual(str(polymer),
                         "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB")

    def test_part2(self):
        pass
