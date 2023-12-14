# coding=utf-8
from abc import ABC, abstractmethod
from typing import Tuple, Dict, Iterable, Iterator, Union, Optional, Any

Pos2D = Tuple[int, int]
Pos3D = Tuple[int, int, int]
PosND = Union[Pos2D, Pos3D]
Charter = Iterable[Iterable[Any]]
Seed = Optional[Dict[PosND, Any]]

CARDINAL_2D = (
    (-1, 0), (1, 0), (0, -1), (0, 1)
)

ALL_2D = CARDINAL_2D + (
    (-1, -1), (1, -1), (-1, 1), (1, 1)
)

CARDINAL_3D = (
    (-1, 0, 0), (1, 0, 0),
    (0, -1, 0), (0, 1, 0),
    (0, 0, -1), (0, 0, 1)
)

ALL_3D = tuple(
    (x, y, z) for z in range(-1, 2) for y in range(-1, 2) for x in range(-1, 2)
    if (x, y, z) != (0, 0, 0)
)


class LoopError(Exception):
    pass


class LinkedNode:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return (
            f"{"<-" if self.prev else ""}{self.val}{"->" if self.prev else ""}"
        )

    def __iter__(self) -> Iterator["LinkedNode"]:
        node = self
        while True:
            yield node
            node = node.next
            if node is None or node is self:
                return

    def append(self, node: "LinkedNode") -> None:
        if self.next is not None:
            raise ValueError("Base Node is already linked.")

        elif node.prev is not None:
            raise ValueError("Append Node is already linked.")

        self.next, node.prev = node, self

    def remove(self) -> "LinkedNode":
        prev_node = self.prev
        prev_node.next, self.next.prev = self.next, prev_node
        self.next, self.prev = None, None
        return prev_node

    def splice(self, node: "LinkedNode") -> None:
        if self.next is None:
            raise ValueError("Base node is not linked.")

        elif (node.next, node.prev) != (None, None):
            raise ValueError("Splice Node is already linked.")

        node.prev, node.next = self, self.next
        self.next = node.next.prev = node

    def seek(self, distance: int) -> "LinkedNode":
        node = self
        for _ in range(abs(distance)):
            node = node.next if distance > 0 else node.prev
            if node is None:
                raise IndexError()

        return node

    def find(self, needle: Any, reverse: bool = False) -> "LinkedNode":
        node = self
        while node.val != needle:
            node = node.prev if reverse else node.next
            if node is None:
                raise ValueError()

            elif node is self:
                raise LoopError()

        return node


class SimpleGrid:
    def __init__(self, charter: Charter) -> None:
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

    def index(self, needle: Any) -> Pos2D:
        for y, line in enumerate(self.state):
            for x, val in enumerate(line):
                if needle == val:
                    return (x, y)
        else:
            raise ValueError(f"{needle} is not in grid.")

    def rows(self) -> Iterator[list[Any]]:
        return iter(self.state)

    def columns(self) -> Iterator[list[Any]]:
        return (
            [self.state[y][x] for y in range(self.size["y"])]
            for x in range(self.size["x"])
        )

    def values(self) -> Iterator[Any]:
        for line in self.state:
            yield from line

    def neighbors(self, position: Pos2D, cardinal: bool = True) -> Iterator[Pos2D]:
        x, y = position
        for delta_x, delta_y in CARDINAL_2D if cardinal else ALL_2D:
            n_x, n_y = x + delta_x, y + delta_y
            if (0 <= n_x < self.size["x"] and 0 <= n_y < self.size["y"]):
                yield (n_x, n_y)


class SparseBase(ABC):
    def __init__(self, seed: Seed = None) -> None:
        self.state = seed or {}

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

    def get(self, position: PosND, default=None) -> Any:
        return self.state.get(position, default)

    def values(self):
        return self.state.values()

    @property
    @abstractmethod
    def size(self) -> Tuple[PosND, PosND]:
        pass

    @staticmethod
    @abstractmethod
    def area(start: PosND, stop: PosND) -> Iterator[PosND]:
        pass

    @abstractmethod
    def neighbors(self, position: PosND, cardinal: bool = True) -> Iterator[PosND]:
        pass


class SparseGrid(SparseBase):
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

    @property
    def size(self) -> Tuple[Pos2D, Pos2D]:
        keys = list(self)
        x_spread = {x for x, _ in keys}
        y_spread = {y for _, y in keys}

        return (
            (min(x_spread), min(y_spread)),
            (max(x_spread), max(y_spread)),
        )

    @staticmethod
    def area(start: Pos2D, stop: Pos2D) -> Iterator[Pos2D]:
        min_x, min_y = start
        max_x, max_y = stop
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                yield (x, y)

    def neighbors(self, position: Pos2D, cardinal: bool = True) -> Iterator[Pos2D]:
        x, y = position
        for delta_x, delta_y in CARDINAL_2D if cardinal else ALL_2D:
            yield (x + delta_x, y + delta_y)


class SparseCube(SparseBase):
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

    @staticmethod
    def area(start: Pos3D, stop: Pos3D) -> Iterator[Pos3D]:
        min_x, min_y, min_z = start
        max_x, max_y, max_z = stop
        for z in range(min_z, max_z + 1):
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    yield (x, y, z)

    def neighbors(self, position: Pos3D, cardinal: bool = True) -> Iterator[Pos3D]:
        x, y, z = position
        directions = CARDINAL_3D if cardinal else ALL_3D
        for delta_x, delta_y, delta_z in directions:
            yield (x + delta_x, y + delta_y, z + delta_z)
