# coding=utf-8
from unittest import TestCase

from collections import Counter
from src.task10 import jolt_differences, valid_arrangements


class TestTask(TestCase):
    def test_jolt_differences(self):
        input_data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        differences = jolt_differences(input_data)
        self.assertDictEqual(dict(Counter(differences)), {1: 7, 3: 5})

        input_data = [
            28, 33, 18, 42, 31, 14, 46, 20, 48,
            47, 24, 23, 49, 45, 19, 38, 39, 11,
            1, 32, 25, 35, 8, 17, 7, 9, 4, 2,
            34, 10, 3
        ]
        differences = jolt_differences(input_data)
        self.assertDictEqual(dict(Counter(differences)), {1: 22, 3: 10})

    def test_arrangements_small(self):
        differences = jolt_differences(
            [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])

        self.assertEqual(valid_arrangements(differences), 8)

    def test_arrangements_large(self):
        differences = jolt_differences([
            28, 33, 18, 42, 31, 14, 46, 20, 48,
            47, 24, 23, 49, 45, 19, 38, 39, 11,
            1, 32, 25, 35, 8, 17, 7, 9, 4, 2,
            34, 10, 3
        ])

        self.assertEqual(valid_arrangements(differences), 19208)
