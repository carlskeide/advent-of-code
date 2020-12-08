#!/usr/bin/env python3
# coding=utf-8

from unittest import TestCase
from task8 import GameConsole, InfiniteLoopError


class TestGameConsole(TestCase):
    def test_infninite_loop(self):
        program = [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6"
        ]

        console = GameConsole(program)

        with self.assertRaises(InfiniteLoopError) as exc:
            console.run()

        line, accumulator = exc.exception.args
        self.assertEqual(line, 1)
        self.assertEqual(accumulator, 5)
