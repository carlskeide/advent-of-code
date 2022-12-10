# coding=utf-8
from ..utils import load_input
from ..models import SimpleGrid


class DangerCave(SimpleGrid):
    def __init__(self, charter):
        super().__init__(map(int, line) for line in charter)
        self[0,0] = 0  # First square is free

    def assign_costs(self):
        searched = []
        for i in range(1, self.size["x"]):

            search_area = (
                [(i, j) for j in range(i)]
                + [(j, i) for j in range(i)]
                + [(i, i)]
            )

            for x, y in search_area:
                if x == 0:
                    cost = self[x, y-1]

                elif y == 0:
                    cost = self[x-1, y]

                else:
                    cost = min(self[x, y-1], self[x-1, y])

                self[x,y] += cost

            searched.extend(search_area)

if __name__ == "__main__":
    task_input = load_input(year=2021, day=15, group_lines=False)
    cave = DangerCave(task_input)

    part1 = cave.assign_costs()
    print(f"Part 1: {cave[-1,-1]}")

    part2 = ""
    print(f"Part 2: {part2}")
