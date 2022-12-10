# coding=utf-8
from unittest import TestCase

from .task11 import *

TEST_STATE = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526"
]


class TestTask(TestCase):
    def test_part1(self):
        cave = GameOfSquids(TEST_STATE)
        for _ in range(10):
            cave.step()

        self.assertEqual(cave.flashes, 204)
        self.assertEqual(cave.state, [
                [0,4,8,1,1,1,2,9,7,6],
                [0,0,3,1,1,1,2,0,0,9],
                [0,0,4,1,1,1,2,5,0,4],
                [0,0,8,1,1,1,1,4,0,6],
                [0,0,9,9,1,1,1,3,0,6],
                [0,0,9,3,5,1,1,2,3,3],
                [0,4,4,2,3,6,1,1,3,0],
                [5,5,3,2,2,5,2,3,5,0],
                [0,5,3,2,2,5,0,6,0,0],
                [0,0,3,2,2,4,0,0,0,0]
            ]
        )

    def test_part2(self):
        cave = GameOfSquids(TEST_STATE)
        cave.run_until_synchronized()
        self.assertEqual(cave.steps, 195)
