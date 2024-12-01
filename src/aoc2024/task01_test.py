# coding=utf-8
from unittest import TestCase

from .task01 import Task


class TestTask(TestCase):
    sample_input = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    ]

    def test_parse_input(self):
        self.assertEqual(
            Task.parse_input(self.sample_input)[:2],
            [
                (3, 4),
                (4, 3)
            ]
        )

    def test_part1(self):
        task = Task(self.sample_input)
        self.assertEqual(task.part1(), 11)

    def test_part2(self):
        task = Task(self.sample_input)
        self.assertEqual(task.part2(), 31)
