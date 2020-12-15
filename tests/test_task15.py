# coding=utf-8
from unittest import TestCase

from src.task15 import memory_game


class TestTask(TestCase):
    def test_memory(self):
        memory = memory_game([0, 3, 6], limit=2020)
        self.assertListEqual(memory[:10], [0, 3, 6, 0, 3, 3, 1, 0, 4, 0])
        self.assertEqual(memory[-1], 436)

        self.assertEqual(memory_game([1, 3, 2], limit=2020)[-1], 1)
        self.assertEqual(memory_game([2, 1, 3], limit=2020)[-1], 10)
        self.assertEqual(memory_game([1, 2, 3], limit=2020)[-1], 27)
        self.assertEqual(memory_game([2, 3, 1], limit=2020)[-1], 78)
        self.assertEqual(memory_game([3, 2, 1], limit=2020)[-1], 438)
        self.assertEqual(memory_game([3, 1, 2], limit=2020)[-1], 1836)
