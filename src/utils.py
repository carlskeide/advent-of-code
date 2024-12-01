# coding=utf-8
from pathlib import Path
from itertools import tee, zip_longest
from typing import Iterable, Iterator, Any

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "private"


def load_input(year: int, day: int, group_lines: bool = False) -> list[str]:
    input_file = DATA_DIR / f"aoc{year}" / f"task{day:02d}.txt"
    with input_file.open('r') as f:
        content = f.read()

    return content.split("\n\n") if group_lines else content.splitlines()


def grouper(iterable: Iterable, n: int, *, incomplete: str = 'fill', fillvalue: Any = None) -> Iterator:
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
