# coding=utf-8
from unittest import TestCase

from .task05 import *


class TestTask(TestCase):
    crate_map = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
    ]

    moves = [
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2"
        ]

    def test_parse_crates(self):
        self.assertDictEqual(
            parse_crates(self.crate_map),
            {
                1: ["Z", "N"],
                2: ["M", "C", "D"],
                3: ["P"]
            }
        )

    def test_part1(self):
        crates = parse_crates(self.crate_map)
        move_crates(crates, self.moves)
        self.assertDictEqual(
            crates,
            {
                1: ["C"],
                2: ["M"],
                3: ["P", "D", "N", "Z"]
            }
        )

    def test_part2(self):
        crates = parse_crates(self.crate_map)
        move_crates(crates, self.moves, batch=True)
        self.assertDictEqual(
            crates,
            {
                1: ["M"],
                2: ["C"],
                3: ["P", "Z", "N", "D"]
            }
        )
