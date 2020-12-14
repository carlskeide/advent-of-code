# coding=utf-8
from unittest import TestCase

from .task14 import parse_program, masked_value, run_program


class TestTask(TestCase):
    sample_program = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0"
    ]

    def test_parse_program(self):
        mask, instructions = parse_program(self.sample_program)

        self.assertEqual(mask, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        self.assertListEqual(instructions, [(8, 11), (7, 101), (8, 0)])

    def test_masked_value(self):
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        self.assertEqual(masked_value(mask, 11), 73)
        self.assertEqual(masked_value(mask, 101), 101)
        self.assertEqual(masked_value(mask, 0), 64)

    def test_run_program(self):
        memory = run_program([self.sample_program, ])
        self.assertDictEqual(memory, {7: 101, 8: 64})
