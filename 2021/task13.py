# coding=utf-8
import re
from . import load_input


class FoldableGrid:
    def __init__(self, dots):
        self.dots = {
            tuple(int(s) for s in dot.split(',')) for dot in dots
        }

    def __str__(self):
        max_x = max(x for x, y in self.dots)
        max_y = max(y for x, y in self.dots)

        return "\n".join(
            "".join(
                "#" if (x, y) in self.dots else " "
                for x in range(max_x + 1)
            ) for y in range(max_y + 1)
        )

    def fold(self, where):
        axis, pos = where.split('=')
        pos = int(pos)
        new_dots = set()
        for dot in self.dots:
            x, y = dot
            if axis == "x" and x > pos:
                dot = (pos - (x - pos), y)
            elif axis == "y" and y > pos:
                dot = (x, pos - (y - pos))

            new_dots.add(dot)

        self.dots = new_dots


if __name__ == "__main__":
    dots, folds = load_input(day=13, group_lines=True)
    folds = [fold.split()[-1] for fold in folds.splitlines()]

    paper = FoldableGrid(dots.splitlines())
    paper.fold(folds[0])
    print(f"Part 1: {len(paper.dots)}")

    for s in folds[1:]:
        paper.fold(s)

    print(f"Part 2:\n{paper}")
