#!/usr/bin/env python3
# coding=utf-8

import re


class Bag:
    def __init__(self, rule):
        color, content = self.parse_rule(rule)
        self.color = color
        self.content = {
            clr: int(qty) for qty, clr
            in self.parse_contents(content)
        }

    def parse_rule(self, text):
        return re.match(r"^(.*) bags contain ([\w\s,]+).", text).groups()

    def parse_contents(self, text):
        if text == "no other bags":
            return []

        return (
            re.match(r"^(\d+) ([a-z\s]+) bags?$", bag.strip()).groups()
            for bag in text.split(",")
        )


def search_bag(bags, bag_color, color):
    if bag_color == color:
        return True

    for inner_color in bags[bag_color].content:
        if search_bag(bags, inner_color, color):
            return True

    else:
        return False


def count_bags(bags, bag_color):
    count = 0
    for inner_color, quantity in bags[bag_color].content.items():
        count += quantity + (quantity * count_bags(bags, inner_color))

    return count


if __name__ == "__main__":
    with open("./task7.input") as f:
        task_input = [line.strip() for line in f.readlines() if line]

    bags = {bag.color: bag for bag in map(Bag, task_input)}
    part1 = [
        search_bag(bags, color, "shiny gold") for color in bags
        if color != "shiny gold"  # Must be nested at least once
    ]
    print(f"Part 1: {sum(part1)}")

    part2 = count_bags(bags, "shiny gold")
    print(f"Part 2: {part2}")
