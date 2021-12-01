# coding=utf-8
from unittest import TestCase

from src.task16 import invalid_fields, match_rules


class TestTask(TestCase):
    def test_invalid_fields(self):
        rules = {
            "class": [(1, 3), (5, 7)],
            "row": [(6, 11), (33, 44)],
            "seat": [(13, 40), (45, 50)]
        }
        nearby = [
            "7,3,47",
            "40,4,50",
            "55,2,20",
            "38,6,12"
        ]

        self.assertFalse(invalid_fields(rules, nearby[0]))
        self.assertEqual(invalid_fields(rules, nearby[1]), 4)
        self.assertEqual(invalid_fields(rules, nearby[2]), 55)
        self.assertEqual(invalid_fields(rules, nearby[3]), 12)

    def test_match_rules(self):
        rules = {
            "class": [(0, 1), (4, 19)],
            "row": [(0, 5), (8, 19)],
            "seat": [(0, 13), (16, 19)]
        }

        nearby = [
            "3,9,18",
            "15,1,5",
            "5,14,9"
        ]

        self.assertEqual(
            match_rules(rules, nearby),
            {"class": 1, "row": 0, "seat": 2})
