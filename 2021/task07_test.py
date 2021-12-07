# coding=utf-8
from unittest import TestCase

from .task07 import *


class TestTask(TestCase):
    crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    def test_fuel_consumption(self):
        self.assertEqual(fuel_consumption(self.crabs, 1), 41)
        self.assertEqual(fuel_consumption(self.crabs, 2), 37)
        self.assertEqual(fuel_consumption(self.crabs, 3), 39)
        self.assertEqual(fuel_consumption(self.crabs, 10), 71)

    def test_least_fuel(self):
        self.assertEqual(least_fuel(self.crabs), 37)

    def test_part2(self):
        pass
