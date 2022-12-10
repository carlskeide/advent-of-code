# coding=utf-8
from pathlib import Path
from itertools import tee

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"


def load_input(year, day, group_lines=False):
    input_file = DATA_DIR / f"aoc{year}" / f"task{day:02d}.txt"
    with input_file.open('r') as f:
        content = f.read()

    return content.split("\n\n") if group_lines else content.splitlines()


def pairwise(iterable):
    """ Included in python >= 3.10 """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
