# coding=utf-8
from unittest import TestCase

from src.task05 import decode, seat_id


class TestTask(TestCase):
    def test_decode(self):
        self.assertEqual(decode("FBFBBFFRLR"), (44, 5))
        self.assertEqual(decode("BFFFBBFRRR"), (70, 7))
        self.assertEqual(decode("FFFBBBFRRR"), (14, 7))
        self.assertEqual(decode("BBFFBBFRLL"), (102, 4))

    def test_seat_id(self):
        self.assertEqual(seat_id(44, 5), 357)
        self.assertEqual(seat_id(70, 7), 567)
        self.assertEqual(seat_id(14, 7), 119)
        self.assertEqual(seat_id(102, 4), 820)
