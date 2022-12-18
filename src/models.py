# coding=utf-8
from typing import Tuple, Dict, Iterable, Iterator, Union, Optional, Any

Pos2D = Tuple[int, int]
Pos3D = Tuple[int, int, int]
PosND = Union[Pos2D, Pos3D]

CARDINAL_NEIGHBORS = (
    (-1, 0), (1, 0), (0, -1), (0, 1)
)

DIAGONAL_NEIGHBORS = CARDINAL_NEIGHBORS + (
    (-1, -1), (1, -1), (-1, 1), (1, 1)
)


class DiagonalMixin:
    _neighbors = DIAGONAL_NEIGHBORS


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

    def __getitem__(self, position: Pos2D) -> Any:
        x, y = position
        return self.state[y][x]

    def __setitem__(self, position: Pos2D, value: Any) -> None:
        x, y = position
        self.state[y][x] = value

    def __iter__(self) -> Iterator[Pos2D]:
        for y in range(self.size["y"]):
            for x in range(self.size["x"]):
                yield (x, y)

    def values(self) -> Iterator[Any]:
        for line in self.state:
            yield from line

    def neighbors(self, position: Pos2D) -> Iterator[Pos2D]:
        x, y = position
        for delta_x, delta_y in self._neighbors:
            n_x, n_y = x + delta_x, y + delta_y
            if (0 <= n_x < self.size["x"] and 0 <= n_y < self.size["y"]):
                yield (n_x, n_y)


class SparseGrid(object):
    _neighbors = CARDINAL_NEIGHBORS

    def __init__(self, seed: Optional[Dict[PosND, Any]] = None) -> None:
        self.state = seed or {}

    def __str__(self) -> str:
        min_edge, max_edge = self.size
        x_range = range(min_edge[0], max_edge[0] + 1)
        y_range = range(max_edge[1], min_edge[1] - 1, -1)

        return "\n".join(
            "".join(
                str(self.get((x, y), "."))
                for x in x_range
            ) for y in y_range
        )

    def __getitem__(self, position: Union[PosND, slice]) -> Any:
        if isinstance(position, slice):
            return (
                self[pos] for pos
                in self.area(position.start, position.stop)
                if pos in self.state
            )

        else:
            return self.state[position]

    def __setitem__(self, position: PosND, value: Any) -> None:
        self.state[position] = value

    def __iter__(self) -> Iterator[PosND]:
        yield from self.state.keys()

    @property
    def size(self) -> Tuple[Pos2D, Pos2D]:
        keys = list(self)
        x_spread = {x for x, _ in keys}
        y_spread = {y for _, y in keys}

        return (
            (min(x_spread), min(y_spread)),
            (max(x_spread), max(y_spread)),
        )

    def area(self, start: Pos2D, stop: Pos2D) -> Iterator[Pos2D]:
        min_x, min_y = start
        max_x, max_y = stop
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                yield (x, y)

    def neighbors(self, position: Pos2D) -> Iterator[Pos2D]:
        x, y = position
        for delta_x, delta_y in self._neighbors:
            yield (x + delta_x, y + delta_y)

    def get(self, position: PosND, default=None) -> Any:
        return self.state.get(position, default)

    def values(self):
        return self.state.values()


class SparseCube(SparseGrid):
    _neighbors = (
        (-1, 0, 0), (1, 0, 0),
        (0, -1, 0), (0, 1, 0),
        (0, 0, -1), (0, 0, 1)
    )

    def __str__(self) -> str:
        min_edge, max_edge = self.size
        x_range = range(min_edge[0], max_edge[0] + 1)
        y_range = range(max_edge[1], min_edge[1] - 1, -1)
        z_range = range(min_edge[2], max_edge[2] + 1)

        return "\n\n".join(
            f"z{z}:\n" + "\n".join(
                "".join(
                    str(self.get((x, y, z), "."))
                    for x in x_range
                ) for y in y_range
            ) for z in z_range
        )

    @property
    def size(self) -> Tuple[Pos3D, Pos3D]:
        keys = list(self)
        x_spread = {x for x, _, _ in keys}
        y_spread = {y for _, y, _ in keys}
        z_spread = {z for _, _, z in keys}

        return (
            (min(x_spread), min(y_spread), min(z_spread)),
            (max(x_spread), max(y_spread), max(z_spread)),
        )

    def area(self, start: Pos3D, stop: Pos3D) -> Iterator[Pos3D]:
        min_x, min_y, min_z = start
        max_x, max_y, max_z = stop
        for z in range(min_z, max_z + 1):
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    yield (x, y, z)

    def neighbors(self, position: Pos3D) -> Iterator[Pos3D]:
        x, y, z = position
        for delta_x, delta_y, delta_z in self._neighbors:
            yield (x + delta_x, y + delta_y, z + delta_z)
