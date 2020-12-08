# coding=utf-8
from pathlib import Path


def load_input(day, group_lines=False):
    with Path(f"./task{day}.input").open('r') as f:
        content = f.read()

    return content.split("\n\n") if group_lines else content.splitlines()
