# coding=utf-8
from ..utils import load_input


class Cup:
    def __init__(self, label):
        self.label = label
        self.next = None


class Ring:
    def __init__(self, labels):
        self.min = min(labels)
        self.max = max(labels)

        self.cups = {}
        prev = None
        for n in labels:
            cup = Cup(n)
            if prev:
                prev.next = cup

            else:
                self.active = cup

            self.cups[n] = prev = cup

        cup.next = self.active

    def subcups(self, target, count):
        cur = self.cups[target].next
        for _ in range(count):
            yield cur.label
            cur = cur.next

    def move(self):
        first = cur = self.active

        moved = []
        for _ in range(3):
            cur = cur.next
            moved.append(cur)

        first.next = self.active = cur.next

        invalid_targets = [cup.label for cup in moved]
        target = first.label - 1
        while target in invalid_targets or target < 1:
            target = target - 1 if target > self.min else self.max

        target_cup = self.cups[target]
        target_cup.next, moved[-1].next = moved[0], target_cup.next


if __name__ == "__main__":
    task_input = load_input(year=2020, day=23)
    cups = [int(n) for n in task_input[0]]
    ring = Ring(cups)

    for _ in range(100):
        ring.move()

    print(f"Part 1: {''.join(str(c) for c in ring.subcups(1, 8))}")

    many_cups = [int(n) for n in task_input[0]]
    many_cups += list(range(max(many_cups) + 1, 1000001))
    ring = Ring(many_cups)
    for _ in range(10000000):
        ring.move()

    cup1, cup2 = ring.subcups(1, 2)
    print(f"Part 2: {cup1 * cup2}")
