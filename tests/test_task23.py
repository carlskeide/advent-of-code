# coding=utf-8
from unittest import TestCase

from src.task23 import move_cups


class TestTask(TestCase):
    def test_move_cups(self):
        test_input = [3, 8, 9, 1, 2, 5, 4, 6, 7]
        self.assertListEqual(
            move_cups(test_input),
            [2, 8, 9, 1, 5, 4, 6, 7, 3]
        )

        cups = test_input[:]
        for _ in range(10):
            cups = move_cups(cups)

        self.assertListEqual(cups, [8, 3, 7, 4, 1, 9, 2, 6, 5])

        cups = test_input[:]
        for _ in range(100):
            cups = move_cups(cups)

        self.assertListEqual(cups, [1, 6, 7, 3, 8, 4, 5, 2, 9])
