# coding=utf-8
from unittest import TestCase

from src.task23 import Ring


class TestRing(TestCase):
    def test_move(self):
        labels = [3, 8, 9, 1, 2, 5, 4, 6, 7]

        ring = Ring(labels)
        self.assertListEqual(
            list(ring.subcups(3, 8)),
            [8, 9, 1, 2, 5, 4, 6, 7]
        )

        ring.move()
        self.assertListEqual(
            list(ring.subcups(2, 8)),
            [8, 9, 1, 5, 4, 6, 7, 3]
        )

        ring = Ring(labels)
        for _ in range(10):
            ring.move()

        self.assertListEqual(
            list(ring.subcups(8, 8)),
            [3, 7, 4, 1, 9, 2, 6, 5]
        )

        ring = Ring(labels)
        for _ in range(100):
            ring.move()

        self.assertListEqual(
            list(ring.subcups(1, 8)),
            [6, 7, 3, 8, 4, 5, 2, 9]
        )
