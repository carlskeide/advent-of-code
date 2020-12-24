# coding=utf-8
from unittest import TestCase

from src.task24 import parse_steps, traverse, flip
from collections import defaultdict


class TestTask(TestCase):
    test_input = [
        "sesenwnenenewseeswwswswwnenewsewsw",
        "neeenesenwnwwswnenewnwwsewnenwseswesw",
        "seswneswswsenwwnwse",
        "nwnwneseeswswnenewneswwnewseswneseene",
        "swweswneswnenwsewnwneneseenw",
        "eesenwseswswnenwswnwnwsewwnwsene",
        "sewnenenenesenwsewnenwwwse",
        "wenwwweseeeweswwwnwwe",
        "wsweesenenewnwwnwsenewsenwwsesesenwne",
        "neeswseenwwswnwswswnw",
        "nenwswwsewswnenenewsenwsenwnesesenew",
        "enewnwewneswsewnwswenweswnenwsenwsw",
        "sweneswneswneneenwnewenewwneswswnese",
        "swwesenesewenwneswnwwneseswwne",
        "enesenwswwswneneswsenwnewswseenwsese",
        "wnwnesenesenenwwnenwsewesewsesesew",
        "nenewswnwewswnenesenwnesewesw",
        "eneswnwswnwsenenwnwnwwseeswneewsenese",
        "neswnwewnwnwseenwseesewsenwsweewe",
        "wseweeenwnesenwwwswnew"
    ]

    def test_parse_steps(self):
        self.assertListEqual(
            parse_steps("esenee"), ["e", "se", "ne", "e"])

        self.assertListEqual(
            parse_steps("nwwswee"), ["nw", "w", "sw", "e", "e"])

    def test_traverse(self):
        floor = defaultdict(int)
        for steps in self.test_input:
            traverse(floor, parse_steps(steps))

        self.assertEqual(len(floor.values()), 15)
        self.assertEqual(sum(floor.values()), 10)

    def test_flip(self):
        floor = defaultdict(int)
        for steps in self.test_input:
            traverse(floor, parse_steps(steps))

        floor = flip(floor)
        self.assertEqual(sum(floor.values()), 15)
        floor = flip(floor)
        self.assertEqual(sum(floor.values()), 12)
        floor = flip(floor)
        self.assertEqual(sum(floor.values()), 25)
