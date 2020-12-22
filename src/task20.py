# coding=utf-8
from . import load_input

import re
import math

MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]


class Tile:
    def __init__(self, text):
        header, *content = text.splitlines()
        self.id = int(re.sub(r"[^\d]", "", header))
        self.content = content
        self.neighbors = {
            "N": None,
            "E": None,
            "S": None,
            "W": None
        }

    def __repr__(self):
        return f"Tile({self.id})"

    def rotate(self):
        self.content = [
            "".join(line[n] for line in self.content[::-1])
            for n in range(len(self.content[0]))
        ]
        self.neighbors = {
            "N": self.neighbors["W"], "E": self.neighbors["N"],
            "S": self.neighbors["E"], "W": self.neighbors["S"]
        }

    def flip(self):
        self.content = self.content[::-1]
        self.neighbors = {
            "N": self.neighbors["S"], "E": self.neighbors["E"],
            "S": self.neighbors["N"], "W": self.neighbors["W"]
        }

    @property
    def edges(self):
        return {
            "N": self.content[0],
            "E": "".join(line[-1] for line in self.content),
            "S": self.content[-1],
            "W": "".join(line[-0] for line in self.content)
        }

    @property
    def area(self):
        return [line[1:-1] for line in self.content[1:-1]]

    def find_neighbors(self, tiles):
        for other in tiles:
            if other.id == self.id:
                continue

            match_edges = list(other.edges.values())
            match_edges += ["".join(reversed(edge)) for edge in match_edges]

            for card, edge in self.edges.items():
                if edge in match_edges:
                    self.neighbors[card] = other
                    break

    def align_neighbor(self, card):
        cards = "NESWSWNE"
        opposite = cards[cards.index(card) + 4]

        neighbor = self.neighbors[card]
        while neighbor.neighbors[opposite] is not self:
            neighbor.rotate()

        if self.edges[card] != neighbor.edges[opposite]:
            neighbor.flip()
            while self.edges[card] != neighbor.edges[opposite]:
                neighbor.rotate()

    @property
    def connections(self):
        return sum(1 for n in self.neighbors.values() if n)


def make_map(tiles, corner):
    while not (corner.neighbors["E"] and corner.neighbors["S"]):
        corner.rotate()

    row = []
    region = [row, ]
    cur = corner
    for n in range(len(tiles)):
        if n == 0:
            pass

        elif cur is None:
            prev = row[0]
            row = []
            region.append(row)

            cur = prev.neighbors["S"]
            prev.align_neighbor("S")

        else:
            prev = row[-1]
            prev.align_neighbor("E")

        row.append(cur)
        cur = cur.neighbors["E"]

    return [
        "".join(tile.area[i] for tile in row)[::-1]
        for row in region for i in range(8)
    ]


def find_monsters(region):
    monster_match = [
        (ri, ci) for ri, row in enumerate(MONSTER)
        for ci, c in enumerate(row)
        if c == "#"
    ]

    monster_tiles = 0
    for row in range(len(region) - 2):
        for col in range(len(region[0]) - 19):
            search_area = [
                region[row][col:col + 20],
                region[row + 1][col:col + 20],
                region[row + 2][col:col + 20]
            ]

            if all(search_area[r][c] == "#" for r, c in monster_match):
                monster_tiles += len(monster_match)

    return monster_tiles


if __name__ == "__main__":
    task_input = load_input(day=20, group_lines=True)
    tiles = [Tile(text) for text in task_input]

    for tile in tiles:
        tile.find_neighbors(tiles)

    corners = [tile for tile in tiles if tile.connections == 2]
    print(f"Part 1: {math.prod(tile.id for tile in corners)}")

    region = make_map(tiles, corners[0])
    for line in region:
        print(line)

    monster_tiles = find_monsters(region)

    rough_waters = sum(row.count("#") for row in region)
    print(f"Part 2: {rough_waters - monster_tiles}")
