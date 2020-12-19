# coding=utf-8
from unittest import TestCase

from src.task19 import valid_message


class TestTask(TestCase):
    def test_valid_message(self):
        rules = {
            "0": "1 2",
            "1": '"a"',
            "2": "1 3 | 3 1",
            "3": '"b"'
        }
        self.assertTrue(valid_message(rules, "aab"))
        self.assertTrue(valid_message(rules, "aba"))
        self.assertFalse(valid_message(rules, "baa"))

        rules = {
            "0": "4 1 5",
            "1": "2 3 | 3 2",
            "2": "4 4 | 5 5",
            "3": "4 5 | 5 4",
            "4": '"a"',
            "5": '"b"'
        }
        self.assertTrue(valid_message(rules, "aaaabb"))
        self.assertTrue(valid_message(rules, "aaabab"))
        self.assertTrue(valid_message(rules, "abbabb"))
        self.assertTrue(valid_message(rules, "abbbab"))
        self.assertTrue(valid_message(rules, "aabaab"))
        self.assertTrue(valid_message(rules, "aabbbb"))
        self.assertTrue(valid_message(rules, "abaaab"))
        self.assertTrue(valid_message(rules, "ababbb"))
        self.assertFalse(valid_message(rules, "baaabb"))
        self.assertFalse(valid_message(rules, "abbbbb"))
