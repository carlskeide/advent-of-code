# coding=utf-8
from unittest import TestCase

from .task20 import Tile


class TestTiles(TestCase):
    def setUp(self):
        self.tile = Tile(
            "Tile 2311:\n"
            "..##.#..#.\n"
            "##..#.....\n"
            "#...##..#.\n"
            "####.#...#\n"
            "##.##.###.\n"
            "##...#.###\n"
            ".#.#.#..##\n"
            "..#....#..\n"
            "###...#.#.\n"
            "..###..###"
        )

    def test_attr(self):
        self.assertEqual(self.tile.id, 2311)

        self.assertDictEqual({
            "N": "..##.#..#.",
            "E": "...#.##..#",
            "S": "..###..###",
            "W": ".#####..#."
        }, self.tile.edges)

        self.assertListEqual([
            "#..#....",
            "...##..#",
            "###.#...",
            "#.##.###",
            "#...#.##",
            "#.#.#..#",
            ".#....#.",
            "##...#.#"
        ], self.tile.area)

    def test_rotate(self):
        self.tile.rotate()
        self.assertDictEqual({
            'E': '..##.#..#.',
            'N': '.#..#####.',
            'S': '#..##.#...',
            'W': '..###..###'
        }, self.tile.edges)

        self.assertListEqual([
            '#.####.#',
            '##...#..',
            '..#.##..',
            '....#.##',
            '..##.##.',
            '#...#...',
            '.#.##...',
            '#.###.#.'
        ], self.tile.area)

    def test_flip(self):
        self.tile.flip()

        self.assertDictEqual({
            "N": "..###..###",
            "E": "#..##.#...",
            "S": "..##.#..#.",
            "W": ".#..#####."
        }, self.tile.edges)

        print(self.tile.area)
        self.assertListEqual([
            '##...#.#',
            '.#....#.',
            '#.#.#..#',
            '#...#.##',
            '#.##.###',
            '###.#...',
            '...##..#',
            '#..#....'
        ], self.tile.area)
