# coding=utf-8
from unittest import TestCase

from .task12 import *


TEST_CAVES = [
    [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end"
    ], [
        "dc-end",
        "HN-start",
        "start-kj",
        "dc-start",
        "dc-HN",
        "LN-dc",
        "HN-end",
        "kj-sa",
        "kj-HN",
        "kj-dc"
    ], [
        "fs-end",
        "he-DX",
        "fs-he",
        "start-DX",
        "pj-DX",
        "end-zg",
        "zg-sl",
        "zg-pj",
        "pj-he",
        "RW-he",
        "fs-DX",
        "pj-RW",
        "zg-RW",
        "start-pj",
        "he-WI",
        "zg-he",
        "pj-fs",
        "start-RW"
    ]
]

class TestTask(TestCase):
    def test_init(self):
        cave = Cave(TEST_CAVES[0])

        self.assertSetEqual(
            set(cave.nodes),
            {"start", "end", "A", "b", "c", "d"})

        self.assertSetEqual(
            cave.nodes["A"],
            {"start", "end", "b", "c"})

        self.assertSetEqual(cave.nodes["d"], {"b"})

    def test_part1(self):
        cave = Cave(TEST_CAVES[0])
        self.assertEqual(len(cave.find_paths()), 10)

        cave = Cave(TEST_CAVES[1])
        self.assertEqual(len(cave.find_paths()), 19)

        cave = Cave(TEST_CAVES[2])
        self.assertEqual(len(cave.find_paths()), 226)

    def test_part2(self):
        pass
