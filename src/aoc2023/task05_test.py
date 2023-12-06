# coding=utf-8
from unittest import TestCase

from .task05 import *


class TestTask(TestCase):
    sample_input = (
        "seeds: 79 14 55 13",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    )

    def test_parse_almanac(self):
        seeds, maps = parse_almanac(self.sample_input)
        self.assertEqual(seeds, [79, 14, 55, 13])
        self.assertEqual(
            maps[("light", "temperature")],
            [
                (range(45, 64), 36),
                (range(64, 77), 4),
                (range(77, 100), -32),
            ]
        )

    def test_find_location(self):
        seeds, maps = parse_almanac(self.sample_input)
        self.assertEqual(find_location(79, maps), 82)
        self.assertEqual(find_location(14, maps), 43)
        self.assertEqual(find_location(55, maps), 86)
        self.assertEqual(find_location(13, maps), 35)
