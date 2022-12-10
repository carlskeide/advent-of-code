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
    def test_polymerize(self):
        polymer = Polymer("NNCB", TEST_RULES)
        counts = polymer.polymerize(10)
        self.assertEqual(sum(counts.values()), 3073)
        self.assertEqual(counts["B"], 1749)
        self.assertEqual(counts["C"], 298)
        self.assertEqual(counts["H"], 161)
        self.assertEqual(counts["N"], 865)
