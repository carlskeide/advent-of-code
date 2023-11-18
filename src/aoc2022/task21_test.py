# coding=utf-8
from unittest import TestCase

from .task21 import *


class TestTask(TestCase):
    def test_part1(self):
        sample_monkeys = {
            "root": ["pppw", "+", "sjmn"],
            "dbpl": 5,
            "cczh": ["sllz", "+", "lgvd"],
            "zczc": 2,
            "ptdq": ["humn", "-", "dvpt"],
            "dvpt": 3,
            "lfqf": 4,
            "humn": 5,
            "ljgn": 2,
            "sjmn": ["drzm", "*", "dbpl"],
            "sllz": 4,
            "pppw": ["cczh", "/", "lfqf"],
            "lgvd": ["ljgn", "*", "ptdq"],
            "drzm": ["hmdt", "-", "zczc"],
            "hmdt": 32
        }

        resolve_monkeys(sample_monkeys)
        self.assertEqual(sample_monkeys["root"], 152)

    def test_part2(self):
        pass
