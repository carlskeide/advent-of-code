# coding=utf-8
from unittest import TestCase

from .task06 import *


class TestTask(TestCase):
    def test_part1(self):
        self.assertEqual(
            find_header("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4), 7)
        self.assertEqual(
            find_header("bvwbjplbgvbhsrlpgdmjqwftvncz", 4), 5)
        self.assertEqual(
            find_header("nppdvjthqldpwncqszvftbrmjlhg", 4), 6)
        self.assertEqual(
            find_header("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4), 10)
        self.assertEqual(
            find_header("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4), 11)

    def test_part2(self):
        self.assertEqual(
            find_header("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14), 19)
        self.assertEqual(
            find_header("bvwbjplbgvbhsrlpgdmjqwftvncz", 14), 23)
        self.assertEqual(
            find_header("nppdvjthqldpwncqszvftbrmjlhg", 14), 23)
        self.assertEqual(
            find_header("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14), 29)
        self.assertEqual(
            find_header("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14), 26)
