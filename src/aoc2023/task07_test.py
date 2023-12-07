# coding=utf-8
from unittest import TestCase

from .task07 import *


class TestTask(TestCase):
    sample_input = [
        ("32T3K", 765),
        ("T55J5", 684),
        ("KK677", 28),
        ("KTJJT", 220),
        ("QQQJA", 483)
    ]

    def test_parse_hand(self):
        self.assertEqual(
            parse_hand("24689", joker=False),
            (0, (2, 4, 6, 8, 9))
        )
        self.assertEqual(
            parse_hand("TJQKA", joker=False),
            (0, (10, 11, 12, 13, 14))
        )
        self.assertEqual(
            parse_hand("TJQKA", joker=True),
            (2, (10, 1, 11, 12, 13))
        )

        self.assertEqual(
            parse_hand("12341", joker=False),
            (2, (1, 2, 3, 4, 1))
        )
        self.assertEqual(
            parse_hand("12312", joker=False),
            (22, (1, 2, 3, 1, 2))
        )
        self.assertEqual(
            parse_hand("12311", joker=False),
            (3, (1, 2, 3, 1, 1))
        )
        self.assertEqual(
            parse_hand("12121", joker=False),
            (32, (1, 2, 1, 2, 1))
        )
        self.assertEqual(
            parse_hand("11211", joker=False),
            (4, (1, 1, 2, 1, 1))
        )
        self.assertEqual(
            parse_hand("11111", joker=False),
            (5, (1, 1, 1, 1, 1))
        )

    def test_part1(self):
        self.assertEqual(
            sorted_hands(self.sample_input, joker=False),
            [
                ("32T3K", 765),
                ("KTJJT", 220),
                ("KK677", 28),
                ("T55J5", 684),
                ("QQQJA", 483),
            ]
        )

    def test_part2(self):
        self.assertEqual(
            sorted_hands(self.sample_input, joker=True),
            [
                ("32T3K", 765),
                ("KK677", 28),
                ("T55J5", 684),
                ("QQQJA", 483),
                ("KTJJT", 220),
            ]
        )
