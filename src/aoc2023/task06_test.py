# coding=utf-8
from unittest import TestCase

from .task06 import *


class TestTask(TestCase):
    sample_input = [
        (7, 9),
        (15, 40),
        (30, 200)
    ]

    def test_winning_times(self):
        self.assertEqual(winning_times(*self.sample_input[0]), 4)
        self.assertEqual(winning_times(*self.sample_input[1]), 8)
        self.assertEqual(winning_times(*self.sample_input[2]), 9)
