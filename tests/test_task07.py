# coding=utf-8
from unittest import TestCase

from src.task07 import Bag


class TestTask(TestCase):
    def setUp(self):
        task_input = [
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."
        ]

        self.bags = {bag.color: bag for bag in map(Bag, task_input)}
        for bag in self.bags.values():
            bag.fill_bag(self.bags)

    def test_bag_search(self):
        matches = {bag.color for bag in self.bags.values() if bag.search("shiny gold")}
        assert matches == {"bright white", "muted yellow", "dark orange", "light red"}

    def test_bag_count(self):
        assert self.bags["shiny gold"].count_contents() == 32

        task_input = [
            "shiny gold bags contain 2 dark red bags.",
            "dark red bags contain 2 dark orange bags.",
            "dark orange bags contain 2 dark yellow bags.",
            "dark yellow bags contain 2 dark green bags.",
            "dark green bags contain 2 dark blue bags.",
            "dark blue bags contain 2 dark violet bags.",
            "dark violet bags contain no other bags."
        ]

        bags = {bag.color: bag for bag in map(Bag, task_input)}
        for bag in bags.values():
            bag.fill_bag(bags)

        assert bags["shiny gold"].count_contents() == 126
