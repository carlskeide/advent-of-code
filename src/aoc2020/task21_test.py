# coding=utf-8
from unittest import TestCase

from .task21 import unsafe_ingredients
from functools import reduce


class TestTask(TestCase):
    def test_unsafe_ingredients(self):
        test_input = [
            [["mxmxvkd", "kfcds", "sqjhc", "nhms"], ["dairy", "fish"]],
            [["trh", "fvjkl", "sbzzf", "mxmxvkd"], ["dairy"]],
            [["sqjhc", "fvjkl"], ["soy"]],
            [["sqjhc", "mxmxvkd", "sbzzf"], ["fish"]]
        ]

        unsafe = unsafe_ingredients(test_input)
        unsafe_items = reduce(set.union, unsafe.values())
        print(unsafe_items)
        self.assertSetEqual(unsafe_items, {'mxmxvkd', 'sqjhc', 'fvjkl'})

        ingredients = []
        for items, _ in test_input:
            ingredients.extend(
                item for item in items if item not in unsafe_items)

        self.assertEqual(len(ingredients), 5)
