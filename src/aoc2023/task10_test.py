# coding=utf-8
from unittest import TestCase

from .task10 import *


class TestTask(TestCase):
    simple_input = (
        ".....",
        ".S-7.",
        ".|.|.",
        ".L-J.",
        ".....",
    )
    complex_input = (
        "7-F7-",
        ".FJ|7",
        "SJLL7",
        "|F--J",
        "LJ.LJ",
    )

    def test_part1(self):
        self.assertEqual(PipeMap(self.simple_input).loop_len(), 8)
        self.assertEqual(PipeMap(self.complex_input).loop_len(), 16)

    def test_part2(self):
        pass
