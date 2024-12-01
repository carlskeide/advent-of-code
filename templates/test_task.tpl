# coding=utf-8
from unittest import TestCase

from .{{ task }} import Task


class TestTask(TestCase):
    sample_input = [
        "",
    ]

    def test_parse_input(self):
        self.assertEqual(
            Task.parse_input(self.sample_input)[0],
            [
                "",
            ]
        )

    def test_part1(self):
        task = Task(self.sample_input)
        self.assertEqual(task.part1(), 0)

    def test_part2(self):
        task = Task(self.sample_input)
        self.assertEqual(task.part2(), 0)
