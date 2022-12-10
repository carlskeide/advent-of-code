# coding=utf-8
import re
from ..utils import load_input
from ..models import SparseGrid


class FoldableGrid(SparseGrid):
    def __init__(self, dots):
        super().__init__({
            tuple(int(s) for s in dot.split(',')): "#" for dot in dots
        })

    def __str__(self):
        return "\n".join(reversed(super().__str__().splitlines()))

    def fold(self, where):
        axis, pos = where.split('=')
        pos = int(pos)
        new_state = {}
        for dot in self:
            x, y = dot
            if axis == "x" and x > pos:
                dot = (pos - (x - pos), y)
            elif axis == "y" and y > pos:
                dot = (x, pos - (y - pos))

            new_state[dot] = "#"

        self.state = new_state


if __name__ == "__main__":
    dots, folds = load_input(year=2021, day=13, group_lines=True)
    folds = [fold.split()[-1] for fold in folds.splitlines()]

    paper = FoldableGrid(dots.splitlines())
    paper.fold(folds[0])
    print(f"Part 1: {len(paper.values())}")

    for s in folds[1:]:
        paper.fold(s)

    print(f"Part 2:\n{paper}")
