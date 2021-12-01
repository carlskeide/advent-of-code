# coding=utf-8
from unittest import TestCase
from itertools import islice

from src.task15 import memory_game


class TestTask(TestCase):
    def test_memory(self):
        memory = list(islice(memory_game([0, 3, 6]), 2020))
        self.assertListEqual(memory[:10], [0, 3, 6, 0, 3, 3, 1, 0, 4, 0])
        self.assertEqual(memory[-1], 436)

        memory = list(islice(memory_game([1, 3, 2]), 2020))
        self.assertEqual(memory[-1], 1)
        memory = list(islice(memory_game([2, 1, 3]), 2020))
        self.assertEqual(memory[-1], 10)
        memory = list(islice(memory_game([1, 2, 3]), 2020))
        self.assertEqual(memory[-1], 27)
        memory = list(islice(memory_game([2, 3, 1]), 2020))
        self.assertEqual(memory[-1], 78)
        memory = list(islice(memory_game([3, 2, 1]), 2020))
        self.assertEqual(memory[-1], 438)
        memory = list(islice(memory_game([3, 1, 2]), 2020))
        self.assertEqual(memory[-1], 1836)
