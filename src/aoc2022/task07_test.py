# coding=utf-8
from unittest import TestCase

from .task07 import *


class TestTask(TestCase):
    sample_output = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]

    def test_parse_output(self):
        fs = parse_output(self.sample_output)
        self.assertDictEqual(
            fs['/'],
            {
                "a": {
                    "e": {
                        "i": 584,
                    },
                    "f": 29116,
                    "g": 2557,
                    "h.lst": 62596,
                },
                "b.txt": 14848514,
                "c.dat": 8504156,
                "d": {
                    "j": 4060174,
                    "d.log": 8033020,
                    "d.ext": 5626152,
                    "k": 7214296,
                }
            }
        )


    def test_rsize(self):
        fs = parse_output(self.sample_output)
        self.assertEqual(rsize(fs["/"]["a"]["e"]), 584)
        self.assertEqual(rsize(fs["/"]["a"]), 94853)
        self.assertEqual(rsize(fs["/"]["d"]), 24933642)
        self.assertEqual(rsize(fs["/"]), 48381165)
