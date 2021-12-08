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

    def test_find_key(self):
        key = find_key([
            "acedgfb", "cdfbe", "gcdfa", "fbcad", "dab",
            "cefabd", "cdfgeb", "eafb", "cagedb", "ab"
        ])

        self.assertSetEqual(key[5], set("cdfeb"))
        self.assertSetEqual(key[3], set("fcadb"))
        self.assertSetEqual(key[2], set("gcdfa"))

        self.assertSetEqual(key[9], set("cefabd"))
        self.assertSetEqual(key[6], set("cdfgeb"))
        self.assertSetEqual(key[0], set("cagedb"))

    def test_decode(self):
        key = find_key([
            "be", "cfbegad", "cbdgef", "fgaecd", "cgeb",
            "fdcge", "agebfd", "fecdb", "fabcd", "edb"
        ])
        self.assertEqual(
            decode(key, ("fdgacbe", "cefdb", "cefbgd", "gcbe")), 8394)
