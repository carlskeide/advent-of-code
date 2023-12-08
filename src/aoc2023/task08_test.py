# coding=utf-8
from unittest import TestCase

from .task08 import *


class TestTask(TestCase):
    def test_part1(self):
        self.assertEqual(traverse(
            "RL", {
                "AAA": ("BBB", "CCC"),
                "BBB": ("DDD", "EEE"),
                "CCC": ("ZZZ", "GGG"),
                "DDD": ("DDD", "DDD"),
                "EEE": ("EEE", "EEE"),
                "GGG": ("GGG", "GGG"),
                "ZZZ": ("ZZZ", "ZZZ")
            }),
            2
        )
        self.assertEqual(traverse(
            "LLR", {
                "AAA": ("BBB", "BBB"),
                "BBB": ("AAA", "ZZZ"),
                "ZZZ": ("ZZZ", "ZZZ")
            }),
            6
        )

    def test_part2(self):
        nodes = {
            "11A": ("11B", "XXX"),
            "11B": ("XXX", "11Z"),
            "11Z": ("11B", "XXX"),
            "22A": ("22B", "XXX"),
            "22B": ("22C", "22C"),
            "22C": ("22Z", "22Z"),
            "22Z": ("22B", "22B"),
            "XXX": ("XXX", "XXX")
        }
        self.assertEqual(traverse("LR", nodes, "11A", r"..Z"), 2)
        self.assertEqual(traverse("LR", nodes, "22A", r"..Z"), 3)

        self.assertEqual(least_steps("LR", nodes), 6)
