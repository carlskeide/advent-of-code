# coding=utf-8
from unittest import TestCase

from src.task22 import combat, score


class TestTask(TestCase):
    def test_combat(self):
        deck1 = [9, 2, 6, 3, 1]
        deck2 = [5, 8, 4, 7, 10]
        result = combat(deck1, deck2)
        self.assertListEqual(result, [3, 2, 10, 6, 8, 5, 9, 4, 7, 1])

    def test_score(self):
        result = score([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
        self.assertEqual(result, 306)
