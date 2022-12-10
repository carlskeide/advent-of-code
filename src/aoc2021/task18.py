# coding=utf-8
from itertools import combinations, chain
from functools import reduce
from operator import add
from math import floor, ceil
from copy import deepcopy
from ..utils import load_input


class SnailFishNumber:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def __getitem__(self, key):
        data = self.data
        for i in key:
            data = data[i]

        return data

    def __setitem__(self, key, value):
        target = self.data
        for i in key[:-1]:
            target = target[i]

        target[key[-1]] = value

    def __add__(self, other):
        new_number = SnailFishNumber(deepcopy([self.data, other.data]))
        new_number.reduce()
        return new_number

    def reduce(self):
        while True:
            try:
                self.explode(path=[])
                self.split(path=[])

            except StopIteration:
                continue  # :-)

            else:
                break

    def explode(self, path):
        if len(path) == 4:
            values = self[path]
            self[path] = 0
            self.overflow(path, values)

            raise StopIteration

        for i in (0, 1):
            if isinstance(self[path + [i]], list):
                self.explode(path + [i])

    def overflow(self, path, values):
        for i in range(1, len(path) + 1):
            base, head = path[:i * -1], path[i * -1]
            for j in (0, 1):
                if values[j] and head == j ^ 1:
                    add_path = base + [j]
                    while isinstance(self[add_path], list):
                        add_path += [j ^ 1]

                    self[add_path] += values[j]
                    values[j] = 0

    def split(self, path):
        if isinstance(self[path], int):
            if self[path] >= 10:
                split = self[path] / 2
                self[path] = [floor(split), ceil(split)]

                raise StopIteration

        else:
            for i in (0, 1):
                self.split(path + [i])

    def get_magnitude(self, path=[]):
        a, b = self[path]

        if isinstance(self[path + [0]], list):
            a = self.get_magnitude(path + [0])

        if isinstance(self[path + [1]], list):
            b = self.get_magnitude(path + [1])

        return a * 3 + b * 2


if __name__ == "__main__":
    task_input = load_input(year=2021, day=18, group_lines=False)
    numbers = [SnailFishNumber(eval(line)) for line in task_input]  # ¯\_(ツ)_/¯
    result = reduce(add, numbers)
    print(f"Part 1: {result.get_magnitude()}")

    sums = (((x + y), (y + x)) for x, y in combinations(numbers, 2))
    magnitudes = (num.get_magnitude() for num in chain.from_iterable(sums))
    print(f"Part 2: {max(magnitudes)}")
