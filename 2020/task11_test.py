# coding=utf-8
from unittest import TestCase

from .task11 import GameOfSeats, GameOfVectorSeats


class TestGameOfSeats(TestCase):
    def setUp(self):
        layout = [
            "L.LL.LL.LL",
            "LLLLLLL.LL",
            "L.L.L..L..",
            "LLLL.LL.LL",
            "L.LL.LL.LL",
            "L.LLLLL.LL",
            "..L.L.....",
            "LLLLLLLLLL",
            "L.LLLLLL.L",
            "L.LLLLL.LL"
        ]
        self.game = GameOfSeats(layout)

    def test_step(self):
        layout_steps = [
            [
                "#.##.##.##",
                "#######.##",
                "#.#.#..#..",
                "####.##.##",
                "#.##.##.##",
                "#.#####.##",
                "..#.#.....",
                "##########",
                "#.######.#",
                "#.#####.##"
            ], [
                "#.LL.L#.##",
                "#LLLLLL.L#",
                "L.L.L..L..",
                "#LLL.LL.L#",
                "#.LL.LL.LL",
                "#.LLLL#.##",
                "..L.L.....",
                "#LLLLLLLL#",
                "#.LLLLLL.L",
                "#.#LLLL.##"
            ], [
                "#.##.L#.##",
                "#L###LL.L#",
                "L.#.#..#..",
                "#L##.##.L#",
                "#.##.LL.LL",
                "#.###L#.##",
                "..#.#.....",
                "#L######L#",
                "#.LL###L.L",
                "#.#L###.##"
            ]
        ]

        self.assertEqual(self.game.step(), layout_steps[0])
        self.assertEqual(self.game.step(), layout_steps[1])
        self.assertEqual(self.game.step(), layout_steps[2])

    def test_run_until_stable(self):
        stable_layout = [
            "#.#L.L#.##",
            "#LLL#LL.L#",
            "L.#.L..#..",
            "#L##.##.L#",
            "#.#L.LL.LL",
            "#.#L#L#.##",
            "..L.L.....",
            "#L#L##L#L#",
            "#.LLLLLL.L",
            "#.#L#L#.##"
        ]
        steps = list(self.game.run_until_stable())
        self.assertEqual(self.game.state, stable_layout)
        self.assertEqual(len(steps), 6)
        self.assertEqual(self.game.occupied_seats, 37)


class TestGameOfVectorSeats(TestCase):
    def setUp(self):
        self.game = GameOfVectorSeats("")

    def test_first_visible(self):
        self.game.state = [
            ".......#.",
            "...#.....",
            ".#.......",
            ".........",
            "..#L....#",
            "....#....",
            ".........",
            "#........",
            "...#....."
        ]
        self.assertEqual(self.game.visible(4, 3).count("#"), 8)

        self.game.state = [
            ".............",
            ".L.L.#.#.#.#.",
            "............."
        ]
        visible = self.game.visible(1, 1)
        self.assertEqual(visible.count("L"), 1)
        self.assertEqual(visible.count("#"), 0)

        self.game.state = [
            ".##.##.",
            "#.#.#.#",
            "##...##",
            "...L...",
            "##...##",
            "#.#.#.#",
            ".##.##."
        ]
        self.assertEqual(self.game.visible(3, 3).count("#"), 0)
