# coding=utf-8
from typing import Tuple, Iterable, Iterator, Any

Position = Tuple[int, int]


class CardinalGrid:
    _neighbors = (
        # Left, Right, Up, Down
        (-1, 0), (1, 0), (0, -1), (0, 1)
    )

    def __init__(self, charter: Iterable[Iterable[Any]]) -> None:
        self.state = [list(line) for line in charter]

        # Width is assumed to be consistent across lines
        self.size = {
            "x": len(self.state[0]),
            "y": len(self.state)
        }

    def __str__(self) -> str:
        return "\n".join("".join(str(i) for i in line) for line in self.state)

    def __getitem__(self, position: Position) -> Any:
        x, y = position
        return self.state[y][x]

    def __setitem__(self, position: Position, value: Any) -> None:
        x, y = position
        self.state[y][x] = value

    def __iter__(self) -> Iterator[Position]:
        for y in range(self.size["y"]):
            for x in range(self.size["x"]):
                yield (x, y)

    def values(self) -> Iterator[Any]:
        for line in self.state:
            yield from line

    def neighbors(self, position: Position) -> Iterator[Position]:
        x, y = position
        for delta_x, delta_y in self._neighbors:
            n_x, n_y = x + delta_x, y + delta_y
            if (0 <= n_x < self.size["x"] and 0 <= n_y < self.size["y"]):
                yield (n_x, n_y)


class DiagonalGrid(CardinalGrid):
    _neighbors = (
        # Up/Left, Up, Up/Right,
        (-1, -1), (0, -1), (1, -1),
        # Left, Right
        (-1, 0), (1, 0),
        # Down/Left, Down, Down/Right
        (-1, 1), (0, 1), (1, 1)
    )
