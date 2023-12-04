# coding=utf-8
from unittest import TestCase

from .task04 import *


class TestTask(TestCase):
    sample_input = (
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    )

    def test_score(self):
        self.assertEqual(0, score(0))
        self.assertEqual(1, score(1))
        self.assertEqual(2, score(2))
        self.assertEqual(8, score(4))

    def test_part1(self):
        parsed_cards = parse_cards(self.sample_input)
        self.assertEqual(
            {
                1: 4,
                2: 2,
                3: 2,
                4: 1,
                5: 0,
                6: 0
            },
            parsed_cards
        )

    def test_part2(self):
        parsed_cards = parse_cards(self.sample_input)
        self.assertEqual(
            {
                1: 1,
                2: 2,
                3: 4,
                4: 8,
                5: 14,
                6: 1
            },
            score_recursive(parsed_cards)
        )
