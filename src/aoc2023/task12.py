# coding=utf-8
import re
from itertools import product, repeat
from ..utils import load_input


def valid_combinations(haystack: str, groups: list[int]) -> int:
    valid_pattern = (
        r"^\.*" + r"\.*".join(
            "((?<!#)" + "#" * size + "(?!#))" for size in groups
        ) + r"\.*$"
    )
    valid = re.compile(valid_pattern)

    replacements = haystack.count("?")
    template = haystack.replace("?", "{}")

    return sum(
        bool(valid.match(template.format(*subs)))
        for subs in product(*(".#" for _ in range(replacements)))
    )


def make_hard(haystack: str, groups: list[int]) -> tuple[str, list[int]]:
    return (
        "?".join(repeat(haystack, 5)),
        groups * 5
    )

if __name__ == "__main__":
    task_input = load_input(year=2023, day=12, group_lines=False)
    patterns = [
        (haystack, [int(s) for s in groups.split(",")])
        for haystack, groups in map(str.split, task_input)
    ]

    part1 = sum(valid_combinations(*args) for args in patterns)
    print(f"Part 1: {part1}")

    part2 = sum(valid_combinations(*make_hard(args)) for args in patterns)
    print(f"Part 2: {part2}")
