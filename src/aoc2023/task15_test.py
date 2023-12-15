# coding=utf-8
from unittest import TestCase

from .task15 import *


class TestTask(TestCase):
    def test_part1(self):
        self.assertEqual(holiday_hash("HASH"), 52)

    def test_lens_map(self):
        sample_steps = (
            "rn=1",
            "cm-",
            "qp=3",
            "cm=2",
            "qp-",
            "pc=4",
            "ot=9",
            "ab=5",
            "pc-",
            "pc=6",
            "ot=7",
        )
        boxes = lens_map(sample_steps)
        self.assertEqual(boxes[0], {"rn": 1, "cm": 2})
        self.assertEqual(boxes[3], {'ot': 7, 'ab': 5, 'pc': 6})

    def test_focus(self):
        self.assertEqual(
            focus({
                0: {"rn": 1, "cm": 2},
                3: {'ot': 7, 'ab': 5, 'pc': 6}
            }),
            145
        )
