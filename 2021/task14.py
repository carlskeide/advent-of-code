# coding=utf-8
from collections import Counter
from . import load_input


class Polymer:
    def __init__(self, seed, rules):
        self.state = list(seed)
        self.rules = {
            tuple(pair): insert
            for pair, insert in (
                rule.split(" -> ") for rule in rules
            )
        }

    def __str__(self):
        return "".join(self.state)

    def step(self):
        new_state = []
        for a, b in (self.state[i:i + 2] for i in range(len(self.state) - 1)):
            new_state.append(a)
            if (a, b) in self.rules:
                new_state.append(self.rules[(a, b)])

        new_state.append(b)

        self.state = new_state


if __name__ == "__main__":
    seed, rules = load_input(day=14, group_lines=True)
    polymer = Polymer(seed, rules.splitlines())

    for _ in range(10):
        polymer.step()

    count = Counter(polymer.state).most_common()
    print(f"Part 1: {count[0][1] - count[-1][1]}")

    part2 = ""
    print(f"Part 2: {part2}")
