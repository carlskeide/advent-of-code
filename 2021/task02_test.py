# coding=utf-8
from unittest import TestCase

from .task02 import Submarine, DeltaSubmarine


class TestTask(TestCase):
    instructions = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2"
    ]

    def test_part1(self):
        submarine = Submarine()
        submarine.run(self.instructions)

        self.assertEqual(submarine.distance, 15)
        self.assertEqual(submarine.depth, 10)

    def test_part2(self):
        submarine = DeltaSubmarine()
        submarine.run(self.instructions)

        self.assertEqual(submarine.distance, 15)
        self.assertEqual(submarine.depth, 60)
