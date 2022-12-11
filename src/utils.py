# coding=utf-8
from pathlib import Path
from itertools import tee, zip_longest

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

def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    """ Collect data into non-overlapping fixed-length chunks or blocks
    from: https://docs.python.org/3/library/itertools.html#itertools-recips
    """
    args = [iter(iterable)] * n

    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')
