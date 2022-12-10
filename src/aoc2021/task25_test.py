# coding=utf-8
from unittest import TestCase

from .task25 import *


class TestGameOfCucumbers(TestCase):
    def test_run_until_stable(self):
        cucumbers = GameOfCucumbers([
            "v...>>.vv>",
            ".vv>>.vv..",
            ">>.>v>...v",
            ">>v>>.>.v.",
            "v>v.vv.v..",
            ">.>>..v...",
            ".vv..>.>v.",
            "v.v..>>v.v",
            "....v..v.>"
        ])

        self.assertEqual(cucumbers.run_until_stable(), 58)

        self.assertListEqual(
            str(cucumbers).splitlines(),
            [
                "..>>v>vv..",
                "..v.>>vv..",
                "..>>v>>vv.",
                "..>>>>>vv.",
                "v......>vv",
                "v>v....>>v",
                "vvv.....>>",
                ">vv......>",
                ".>v.vv.v.."
            ]
        )
