# coding=utf-8
from unittest import TestCase

from .task07 import *


class TestTask(TestCase):
    crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    def test_linear_fuel(self):
        self.assertEqual(linear_fuel(self.crabs, 1), 41)
        self.assertEqual(linear_fuel(self.crabs, 2), 37)
        self.assertEqual(linear_fuel(self.crabs, 3), 39)
        self.assertEqual(linear_fuel(self.crabs, 10), 71)

    def test_exponential_fuel(self):
        self.assertEqual(exponential_fuel(self.crabs, 2), 206)
        self.assertEqual(exponential_fuel(self.crabs, 5), 168)
