# coding=utf-8
import operator

from ..utils import load_input


class DLLItem:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def seek(item, num):
    for _ in range(abs(num)):
        item = item.next if num > 0 else item.prev

    return item


def build_list(seed, rounds):
    items = [DLLItem(i) for i in seed]

    zero = None
    prev_item = items[-1]
    for item in items:
        prev_item.next = item
        item.prev = prev_item
        prev_item = item
        if item.val == 0:
            zero = item

    for _ in range(rounds):
        mix(items)

    return zero


def mix(items):
    length = len(items)
    for item in items:
        distance = item.val % (length - 1)
        if 0 in (item.val, distance):
            continue

        item.prev.next, item.next.prev = item.next, item.prev

        insert = seek(item.prev, distance)
        item.prev, item.next = insert, insert.next
        item.prev.next = item.next.prev = item


if __name__ == "__main__":
    task_input = [int(line) for line in load_input(year=2022, day=20)]

    zero = build_list(task_input, rounds=1)
    part1 = sum(seek(zero, n).val for n in (1000, 2000, 3000))
    print(f"Part 1: {part1}")

    part2_input = (i * 811589153 for i in task_input)
    zero = build_list(part2_input, rounds=10)
    part2 = sum(seek(zero, n).val for n in (1000, 2000, 3000))
    print(f"Part 2: {part2}")
