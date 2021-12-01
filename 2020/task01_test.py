# coding=utf-8
from unittest import TestCase

from src.task01 import find_expences


class TestTask(TestCase):
    def test_find_expences(self):
        input_data = [
            1721,
            979,
            366,
            299,
            675,
            1456
        ]

        self.assertEqual(find_expences(input_data, 2), 514579)
        self.assertEqual(find_expences(input_data, 3), 241861950)
