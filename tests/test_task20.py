# coding=utf-8
from unittest import TestCase

from src.task20 import parse_tile


class TestTiles(TestCase):
    def test_parse_tile(self):
        tile = (
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

        tile_id, edges = parse_tile(tile)
        self.assertEqual(tile_id, "2311")
        self.assertListEqual(
            ["..##.#..#.", "...#.##..#", "..###..###", ".#####..#."], edges)
