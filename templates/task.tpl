# coding=utf-8
from typing import Any

from .. import BaseTask


class Task(BaseTask):
    @staticmethod
    def parse_input(task_input: list[str]) -> Any:
        return task_input

    def part1(self) -> int:
        return 0

    def part2(self) -> int:
        return 0
