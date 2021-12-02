# coding=utf-8
from unittest import TestCase

from .task02 import Submarine


class TestTask(TestCase):
    def test_part1(self):
        instructions = [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"
        ]

        submarine = Submarine()
        submarine.run(instructions)

        self.assertEqual(submarine.distance, 15)
        self.assertEqual(submarine.depth, 10)
