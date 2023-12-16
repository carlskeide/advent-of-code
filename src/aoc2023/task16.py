# coding=utf-8
from itertools import chain
from ..utils import load_input
from ..models import SimpleGrid, Charter, Pos2D

mirrors = {
    "/": {"n": "e", "e": "n", "s": "w", "w": "s"},
    "\\": {"n": "w", "w": "n", "s": "e", "e": "s"}
}

splitters = {
    "-": {"n": "ew","s": "ew"},
    "|": {"e": "ns", "w": "ns"}
}

class LightMap(SimpleGrid):
    def run(self, position: Pos2D, heading: str) -> int:
        cache = set()
        cursors = [
            (position, heading)
        ]

        while cursors:
            cursor = cursors.pop()
            if cursor in cache:
                continue

            cache.add(cursor)

            pos, heading = cursor
            tile = self[pos]

            if (mirror := mirrors.get(tile)):
                heading = mirror[heading]

            elif (splitter := splitters.get(tile, "")) :
                heading = splitter.get(heading, heading)

            for head in heading:
                try:
                    cursors.append((self.neighbor(pos, head), head))
                except IndexError:
                    continue

        return len({pos for pos, _ in cache})

    def best_run(self) -> int:
        results = set()
        max_x = self.size["x"] - 1
        max_y = self.size["y"] - 1

        for x in range(self.size["x"]):
            results.add(self.run((x, 0), "s"))
            results.add(self.run((x, max_y), "n"))

        for y in range(self.size["y"]):
            results.add(self.run((0, y), "e"))
            results.add(self.run((max_x, y), "w"))

        return max(results)


if __name__ == "__main__":
    task_input = load_input(year=2023, day=16, group_lines=False)

    lightmap = LightMap(task_input)
    part1 = lightmap.run((0, 0), "e")
    print(f"Part 1: {part1}")

    part2 = lightmap.best_run()
    print(f"Part 2: {part2}")
