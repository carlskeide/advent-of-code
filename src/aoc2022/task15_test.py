# coding=utf-8
from unittest import TestCase

from .task15 import *


class TestTask(TestCase):
    sample_input = [
        {"sensor": (2, 18), "beacon": (-2, 15)},
        {"sensor": (9, 16), "beacon": (10, 16)},
        {"sensor": (13, 2), "beacon": (15, 3)},
        {"sensor": (12, 14), "beacon": (10, 16)},
        {"sensor": (10, 20), "beacon": (10, 16)},
        {"sensor": (14, 17), "beacon": (10, 16)},
        {"sensor": (8, 7), "beacon": (2, 10)},
        {"sensor": (2, 0), "beacon": (2, 10)},
        {"sensor": (0, 11), "beacon": (2, 10)},
        {"sensor": (20, 14), "beacon": (25, 17)},
        {"sensor": (17, 20), "beacon": (21, 22)},
        {"sensor": (16, 7), "beacon": (15, 3)},
        {"sensor": (14, 3), "beacon": (15, 3)},
        {"sensor": (20, 1), "beacon": (15, 3)}
    ]

    def test_parse_sensor(self):
        self.assertEqual(
            parse_sensor(
                "Sensor at x=2, y=18: closest beacon is at x=-2, y=15"
            ),
            {"sensor": (2, 18), "beacon": (-2, 15)}
        )

    def test_part1(self):
        zone = Zone(self.sample_input, watch_row=10)
        self.assertEqual(len(zone.empty), 26)

    def test_part2(self):
        pass

