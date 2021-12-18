# coding=utf-8
from unittest import TestCase

from .task17 import *


class TestTask(TestCase):
    def test_parse_target(self):
        self.assertEqual(
            parse_target("target area: x=124..174, y=-123..-86"),
            (124, 174, -86, -123))

    def test_max_height(self):
        self.assertEqual(max_height((20, 30, -5, -10)), 45)
