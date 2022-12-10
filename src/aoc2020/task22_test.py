# coding=utf-8
from unittest import TestCase

from .task22 import combat, recursive_combat, score


class TestTask(TestCase):
    def setUp(self):
        self.decks = [
            [9, 2, 6, 3, 1],
            [5, 8, 4, 7, 10]
        ]

    def test_combat(self):
        result = combat(self.decks[0], self.decks[1])
        self.assertListEqual(result, [3, 2, 10, 6, 8, 5, 9, 4, 7, 1])

    def test_recursive_combat(self):
        result = recursive_combat(self.decks[0], self.decks[1])
        self.assertTupleEqual(result, ([], [7, 5, 6, 2, 4, 1, 10, 8, 9, 3]))

    def test_score(self):
        result = score([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
        self.assertEqual(result, 306)
