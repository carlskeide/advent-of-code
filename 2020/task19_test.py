# coding=utf-8
from unittest import TestCase

from .task19 import valid_message


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

    def test_valid_recursive(self):

        rules = {
            "42": "9 14 | 10 1",
            "9": "14 27 | 1 26",
            "10": "23 14 | 28 1",
            "1": '"a"',
            "11": "42 31",
            "5": "1 14 | 15 1",
            "19": "14 1 | 14 14",
            "12": "24 14 | 19 1",
            "16": "15 1 | 14 14",
            "31": "14 17 | 1 13",
            "6": "14 14 | 1 14",
            "2": "1 24 | 14 4",
            "0": "8 11",
            "13": "14 3 | 1 12",
            "15": "1 | 14",
            "17": "14 2 | 1 7",
            "23": "25 1 | 22 14",
            "28": "16 1",
            "4": "1 1",
            "20": "14 14 | 1 15",
            "3": "5 14 | 16 1",
            "27": "1 6 | 14 18",
            "14": '"b"',
            "21": "14 1 | 1 14",
            "25": "1 1 | 1 14",
            "22": "14 14",
            "8": "42",
            "26": "14 22 | 1 20",
            "18": "15 15",
            "7": "14 5 | 1 21",
            "24": "14 1"
        }

        messages = [
            "aaaabbaaaabbaaa",
            "bbabbbbaabaabba",
            "ababaaaaaabaaab",
            "ababaaaaabbbaba",
            "aaaaabbaabaaaaababaa",
            "bbbbbbbaaaabbbbaaabbabaaa",
            "baabbaaaabbaaaababbaababb",
            "babbbbaabbbbbabbbbbbaabaaabaaa",
            "abbbbabbbbaaaababbbbbbaaaababb",
            "babaaabbbaaabaababbaabababaaab",
            "bbbababbbbaaaaaaaabbababaaababaabab",
            "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
            "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba",
            "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
            "abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa"
        ]

        matching = (valid_message(rules, msg) for msg in messages)
        self.assertEqual(sum(matching), 3)

        rules["8"] = "42 | 42 R"
        rules["11"] = "42 31 | 42 R 31"

        matching = (valid_message(rules, msg) for msg in messages)
        self.assertEqual(sum(matching), 12)
