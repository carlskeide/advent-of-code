# coding=utf-8
from .. import BaseTask

from collections import Counter
from typing import Any


class Task(BaseTask):
    @staticmethod
    def parse_input(task_input: list[str]) -> Any:
        return [
            tuple(int(s) for s in line.split())
            for line in task_input
        ]

    def part1(self) -> int:
        return sum(
            abs(a - b)
            for a, b in zip(
                sorted(t[0] for t in self.input),
                sorted(t[1] for t in self.input)
            )
        )

    def part2(self) -> int:
        duplicates = Counter(t[1] for t in self.input)
        return sum(t[0] * duplicates[t[0]] for t in self.input)
