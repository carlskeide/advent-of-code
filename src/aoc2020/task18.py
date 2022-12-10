# coding=utf-8
from ..utils import load_input

from operator import add, mul


def ltr_maths(expr):
    mem = 0
    i = 0
    op = add
    while i < len(expr):
        c = expr[i]
        i += 1

        if c.isnumeric():
            mem = op(mem, int(c))
        elif c == "+":
            op = add
        elif c == "*":
            op = mul
        elif c == "(":
            skip, res = ltr_maths(expr[i:])
            i += skip
            mem = op(mem, res)
        elif c == ")":
            return i, mem

    return mem


def parenthezise(expr):
    return "(" + expr.replace(' ', '').replace('(', '((').replace(')', '))').replace('*', ')*(') + ")"


if __name__ == "__main__":
    task_input = load_input(year=2020, day=18, group_lines=False)

    results = (ltr_maths(expr) for expr in task_input)
    print(f"Part 1: {sum(results)}")

    results = (ltr_maths(expr) for expr in map(parenthezise, task_input))
    print(f"Part 2: {sum(results)}")
