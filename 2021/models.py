# coding=utf-8
from typing import Tuple, Dict, Iterable, Iterator, Optional, Any

Position = Tuple[int, int]

CARDINAL_NEIGHBORS = (
    (-1, 0), (1, 0), (0, -1), (0, 1)
)

DIAGONAL_NEIGHBORS = CARDINAL_NEIGHBORS + (
    (-1, -1), (1, -1), (-1, 1), (1, 1)
)


class SimpleGrid:
    _neighbors = CARDINAL_NEIGHBORS

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


class SparseGrid(object):
    _neighbors = CARDINAL_NEIGHBORS

    def __init__(self, seed: Optional[Dict[Position, Any]] = None) -> None:
        self.state = seed or {}

    def __str__(self) -> str:
        keys = list(self)
        x_spread = [x for x, _ in keys]
        y_spread = [y for _, y in keys]
        x_range = range(min(x_spread), max(x_spread) + 1)
        y_range = range(max(y_spread), min(y_spread) - 1, -1)

        return "\n".join(
            "".join(
                self.get((x, y), ".")
                for x in x_range
            ) for y in y_range
        )

    def __getitem__(self, position: Position) -> Any:
        return self.state[position]

    def __setitem__(self, position: Position, value: Any) -> None:
        self.state[position] = value

    def __iter__(self) -> Iterator[Position]:
        yield from self.state.keys()

    def get(self, position: Position, default=None) -> Any:
        return self.state.get(position, default)

    def values(self):
        return self.state.values()


class DiagonalMixin:
    _neighbors = DIAGONAL_NEIGHBORS
