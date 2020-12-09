#!/usr/bin/env python3
# coding=utf-8

from unittest import TestCase
from .task8 import GameConsole, InstructionError, OOBError, InfiniteLoopError


class TestGameConsole(TestCase):
    def test_nop(self):
        console = GameConsole(["nop +1"])
        self.assertEqual(console.accumulator, 0)

    def test_acc(self):
        result = GameConsole(["acc +1"]).run()
        self.assertEqual(result, 1)
        result = GameConsole(["acc +1", "acc +2"]).run()
        self.assertEqual(result, 3)
        result = GameConsole(["acc -1"]).run()
        self.assertEqual(result, -1)
        result = GameConsole(["acc -99"]).run()
        self.assertEqual(result, -99)

    def test_jmp(self):
        result = GameConsole([
            "jmp +2",
            "acc +99",
            "acc +1"
        ]).run()
        self.assertEqual(result, 1)

    def test_unk(self):
        with self.assertRaises(InstructionError):
            GameConsole(["unk +1"]).run()

    def test_oob_jump(self):
        with self.assertRaises(OOBError):
            GameConsole(["jmp -1"]).run()

        with self.assertRaises(OOBError):
            GameConsole(["jmp +4"]).run()

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

        program[7] = program[7].replace("jmp", "nop")
        console = GameConsole(program)
        console.run()
