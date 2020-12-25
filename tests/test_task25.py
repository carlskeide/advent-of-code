# coding=utf-8
from unittest import TestCase

from src.task25 import transform, find_loop_size


class TestCrypto(TestCase):
    def test_transform(self):
        self.assertEqual(transform(7, loop_size=8), 5764801)
        self.assertEqual(transform(7, loop_size=11), 17807724)

        self.assertEqual(transform(17807724, loop_size=8), 14897079)
        self.assertEqual(transform(5764801, loop_size=11), 14897079)

    def test_find_loop_size(self):
        self.assertEqual(find_loop_size(5764801), 8)
        self.assertEqual(find_loop_size(17807724), 11)
