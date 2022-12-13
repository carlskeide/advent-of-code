# coding=utf-8
from unittest import TestCase

from .task09 import *


class TestTask(TestCase):
    sample_instructions = [
        ("R", 4),
        ("U", 4),
        ("L", 3),
        ("D", 1),
        ("R", 4),
        ("D", 1),
        ("L", 5),
        ("R", 2)
    ]

    def test_part1(self):
        rope = Rope()
        for direction, distance in self.sample_instructions:
            rope.move(direction, distance)

        self.assertEqual(len(rope.values()), 13)

        self.assertEqual(rope.head, (2,-2))
        self.assertEqual(rope.tail, (1,-2))

    def test_part2(self):
        pass
