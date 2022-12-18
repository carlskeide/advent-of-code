# coding=utf-8
from itertools import cycle

from ..utils import load_input
from ..models import SparseGrid


TETROMINOES = [
    (
        "####",
    ),
    (
        " # ",
        "###",
        " # "
    ),
    (
        "  #",
        "  #",
        "###"
    ),
    (
        "#",
        "#",
        "#",
        "#"
    ),
    (
        "##",
        "##"
    )
]


class Tetris(SparseGrid):
    def __init__(self, winds):
        super().__init__()
        self.winds = cycle(winds)
        self.pieces = cycle(TETROMINOES)

        self.start_pos = (2, 4)
        for x in range(7):
            self[(x, 0)] = "="

    def play(self):
        piece = list(reversed(next(self.pieces)))
        last_x, last_y = self.start_pos

        while True:
            wind = next(self.winds)
            next_pos = (last_x + (1 if wind == ">" else -1), last_y)
            if self.does_fit(piece, next_pos):
                last_x, last_y = next_pos

            next_pos = (last_x, last_y - 1)
            if self.does_fit(piece, next_pos):
                last_x, last_y = next_pos

            else:
                break

        for y, row in enumerate(piece):
            for x, col in enumerate(row):
                if col == "#":
                    self[(last_x + x, last_y + y)] = "#"

        self.start_pos = (2, self.height + 4)

    def does_fit(self, piece, pos):
        pos_x, pos_y = pos
        for y, row in enumerate(piece):
            for x, col in enumerate(row):
                if col == "#":
                    check_x, check_y = pos_x + x, pos_y + y
                    if self.get((check_x, check_y)) or check_x < 0 or check_x > 6:
                        return False

        else:
            return True

    @property
    def height(self):
        min_edge, max_edge = self.size
        max_x, max_y = max_edge
        return max_y



if __name__ == "__main__":
    task_input = load_input(year=2022, day=17)[0]

    game = Tetris(task_input)
    for _ in range(2022):
        game.play()

    print(f"Part 1: {game.height}")

    part2 = ""
    print(f"Part 2: {part2}")
