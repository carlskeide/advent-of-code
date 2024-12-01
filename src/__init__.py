import logging
import re
import resource

from abc import ABC, abstractmethod
from contextlib import contextmanager
from time import time
from typing import Any, Optional

from .utils import load_input

logging.basicConfig(
    format="%(asctime)s %(name)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG
)


class BaseTask(ABC):
    def __init__(self, task_input: Optional[list[str]] = None) -> None:
        self.start_time = time()

        task_date = re.match(
            r'.*(?:aoc(?P<year>\d+))\.(?:task(?P<day>\d+))',
            self.__module__
        )
        if task_date is None:
            raise Exception("Task date parsing failed.")

        self.year = int(task_date["year"])
        self.day = int(task_date["day"])

        self.log = logging.getLogger(f"{self.year}.{self.day:02d}")

        with self.timed("parse"):
            self.input = self.parse_input(
                task_input or load_input(self.year, self.day))

    @staticmethod
    def parse_input(task_input: list[str]) -> Any:
        return task_input

    @abstractmethod
    def part1(self) -> int:
        pass

    @abstractmethod
    def part2(self) -> int:
        pass

    def run(self) -> None:
        with self.timed("part1"):
            part1_result = self.part1()
            self.log.info(f"Result: {part1_result}")

        with self.timed("part2"):
            part2_result = self.part2()
            self.log.info(f"Result: {part2_result}")

        task_memory_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        self.log.info(f"Total time: {time() - self.start_time:0.3f}s")
        self.log.debug(f"Max RSS: {task_memory_kb / 1024:.1f}mb")

    @contextmanager
    def timed(self, name: str) -> logging.Logger:
        start_time = time()
        prev_name = self.log.name
        self.log.name = f"{prev_name}.{name}"

        self.log.debug(f"Begin")
        yield
        self.log.debug(f"End. Duration: {time() - start_time:0.3f}s")

        self.log.name = prev_name
