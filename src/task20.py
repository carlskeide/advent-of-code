# coding=utf-8
from . import load_input

import re
import math
from collections import Counter


def parse_tile(text):
    header, *tile = text.splitlines()

    tile_id = re.sub(r"[^\d]", "", header)
    edges = [
        tile[0], "".join(line[-1] for line in tile),
        tile[-1], "".join(line[-0] for line in tile)
    ]
    return tile_id, edges


def match_edges(tile_id, tiles):
    my_edges = tiles[tile_id]
    my_edges += ["".join(reversed(edge)) for edge in my_edges]

    matches = []
    for other_id, edges in tiles.items():
        if other_id == tile_id:
            continue
        for edge in edges:
            if edge in my_edges:
                matches.append(other_id)
                break

    return matches


if __name__ == "__main__":
    task_input = load_input(day=20, group_lines=True)
    tiles = {_id: edges for _id, edges in map(parse_tile, task_input)}
    print(f"there are {len(tiles)} tiles to match")

    matches = {}
    for tile_id in tiles:
        matches[tile_id] = match_edges(tile_id, tiles)

    print(f"Matched: {Counter(len(others) for others in matches.values())}")
    corners = (int(tile_id) for tile_id, others
               in matches.items() if len(others) == 2)

    print(f"Part 1: {math.prod(corners)}")
