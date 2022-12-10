# coding=utf-8
from ..utils import load_input


class GameOfSeats:
    threshold = 4

    def __init__(self, layout):
        self.state = layout
        self.last_state = None

    def step(self):
        new_state = []
        for row in range(len(self.state)):
            new_state.append("")
            for col in range(len(self.state[row])):
                seat = self.state[row][col]
                visible = self.visible(row, col)
                if seat == "L" and not visible.count("#"):
                    seat = '#'

                elif seat == "#" and visible.count("#") >= self.threshold:
                    seat = 'L'

                new_state[row] += seat

        self.last_state = self.state
        self.state = new_state
        return new_state

    def visible(self, row, col):
        tiles = ""
        num_rows = len(self.state)
        num_cols = len(self.state[0])
        for r in range(row - 1, row + 2):
            if 0 <= r < num_rows:
                for c in range(col - 1, col + 2):
                    if 0 <= c < num_cols and (r, c) != (row, col):
                        tiles += self.state[r][c]

        return tiles

    def run_until_stable(self):
        while self.state != self.last_state:
            yield self.step()

    @property
    def occupied_seats(self):
        return sum(row.count("#") for row in self.state)


class GameOfVectorSeats(GameOfSeats):
    threshold = 5

    def visible(self, row, col):
        tiles = ""
        vectors = (
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)
        )
        num_rows = len(self.state)
        num_cols = len(self.state[0])
        for dx, dy in vectors:
            tiles += self._first_seat(row, col, dx, dy, num_rows, num_cols)

        return tiles

    def _first_seat(self, row, col, dx, dy, num_rows, num_cols):
        while True:
            row += dx
            col += dy
            if not (0 <= row < num_rows and 0 <= col < num_cols):
                return ""

            if self.state[row][col] in "L#":
                return self.state[row][col]


if __name__ == "__main__":
    task_input = load_input(year=2020, day=11)

    game = GameOfSeats(task_input)
    list(game.run_until_stable())
    print(f"Part 1: {game.occupied_seats}")

    game = GameOfVectorSeats(task_input)
    list(game.run_until_stable())
    print(f"Part 2: {game.occupied_seats}")
