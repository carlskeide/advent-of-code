# coding=utf-8
import re
from ..utils import load_input
from ..models import SparseCube


def parse_instruction(description):
    state, area = description.split()
    matched = re.match(
        r"^.*x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", area)
    x1, x2, y1, y2, z1, z2 = map(int, matched.groups())
    return (
        state,
        (min(x1, x2), min(y1, y2), min(z1, z2)),
        (max(x1, x2), max(y1, y2), max(z1, z2)))


class Reactor(SparseCube):
    def toggle(self, area_min, area_max, state):
        for position in self.area(area_min, area_max):
            self[position] = int(state == "on")


if __name__ == "__main__":
    task_input = load_input(year=2021, day=22, group_lines=False)
    operations = [parse_instruction(s) for s in task_input]

    reactor = Reactor()
    for state, slice_min, slice_max in operations[:20]:
        print(f"Running operation: {state, slice_min, slice_max}")
        reactor.toggle(slice_min, slice_max, state)

    print(f"Part 1: {sum(reactor.values())}")
