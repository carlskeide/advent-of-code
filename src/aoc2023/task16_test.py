# coding=utf-8
from unittest import TestCase

from .task16 import *


class TestTask(TestCase):
    sample_input = (
            ".|...\\....",
            "|.-.\\.....",
            ".....|-...",
            "........|.",
            "..........",
            ".........\\",
            "..../.\\\\..",
            ".-.-/..|..",
            ".|....-|.\\",
            "..//.|....",
        )

    def test_part1(self):
        lightmap = LightMap(self.sample_input)
        self.assertEqual(lightmap.run((0, 0), "e"), 46)

    def test_part2(self):
        lightmap = LightMap(self.sample_input)
        self.assertEqual(lightmap.best_run(), 51)
