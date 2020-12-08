# coding=utf-8
from utils import load_input

import re


class Bag:
    def __init__(self, rule):
        color, content = self.parse_rule(rule)
        self.color = color
        self.charter = [
            (int(quantity), color) for quantity, color
            in self.parse_contents(content)
        ]

        self.content = []

    @staticmethod
    def parse_rule(text):
        return re.match(r"^(.*) bags contain ([\w\s,]+).", text).groups()

    @staticmethod
    def parse_contents(text):
        if text == "no other bags":
            return []

        return (
            re.match(r"^(\d+) ([a-z\s]+) bags?$", bag.strip()).groups()
            for bag in text.split(",")
        )

    def fill_bag(self, all_bags):
        for quantity, color in self.charter:
            self.content.extend(quantity * [all_bags[color]])

    def search(self, color):
        for bag in set(self.content):
            if bag.color == color or bag.search(color):
                return True

        else:
            return False

    def count_contents(self):
        return sum(bag.count_contents() + 1 for bag in self.content)


if __name__ == "__main__":
    bags = {bag.color: bag for bag in map(Bag, load_input(day=7))}
    for bag in bags.values():
        bag.fill_bag(bags)

    part1 = [bag.search("shiny gold") for bag in bags.values()]
    print(f"Part 1: {sum(part1)}")

    part2 = bags["shiny gold"].count_contents()
    print(f"Part 2: {part2}")
