# coding=utf-8
from unittest import TestCase

from .task08 import *


class TestTask(TestCase):
    def test_infer(self):
        self.assertEqual(
            list(infer_basic(("fcgedb", "cgb", "dgebacf", "gc"))),
            [None, 7, 8, 1]
        )

        self.assertEqual(
            list(infer_basic(("fdgacbe", "cefdb", "cefbgd", "gcbe"))),
            [8, None, None, 4]
        )
