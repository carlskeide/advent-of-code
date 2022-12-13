# coding=utf-8
from unittest import TestCase

from .task09 import *


class TestTask(TestCase):
    simple_instructions = [
        ("R", 4),
        ("U", 4),
        ("L", 3),
        ("D", 1),
        ("R", 4),
        ("D", 1),
        ("L", 5),
        ("R", 2)
    ]
    complex_instructions = [
        ("R", 5),
        ("U", 8),
        ("L", 8),
        ("D", 3),
        ("R", 17),
        ("D", 10),
        ("L", 25),
        ("U", 20)
    ]

    def test_short_rope(self):
        rope = Rope(length=2)
        for direction, distance in self.simple_instructions:
            rope.move(direction, distance)

        self.assertEqual(len(rope.values()), 13)
        self.assertEqual(rope.nodes, [(2,-2), (1,-2)])

    def test_long_rope(self):
        rope = Rope(length=10)
        for direction, distance in self.simple_instructions:
            rope.move(direction, distance)

        self.assertEqual(len(rope.values()), 1)

    def test_long_rope_complex(self):
        rope = Rope(length=10)
        for direction, distance in self.complex_instructions:
            rope.move(direction, distance)

        self.assertEqual(len(rope.values()), 36)
