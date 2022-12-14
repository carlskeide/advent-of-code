# coding=utf-8
from unittest import TestCase

from .task11 import *


class TestTask(TestCase):
    def test_parse_monkey(self):
        monkey_text = (
            "Monkey 0:",
            "Starting items: 79, 98",
            "Operation: new = old * 19",
            "Test: divisible by 23",
            "If true: throw to monkey 2",
            "If false: throw to monkey 3"
        )
        self.assertDictEqual(
            parse_monkey(monkey_text),
            {
                "id": 0,
                "items": [79, 98],
                "operation": "{x} * 19",
                "test": {"div": 23, True: 2, False: 3},
                "count": 0
            }
        )

    def test_part1(self):
        monkeys = {
            0: {
                "items": [79, 98],
                "operation": "{x} * 19",
                "test": {"div": 23, True: 2, False: 3},
                "count": 0
            },
            1: {
                "items": [54, 65, 75, 74],
                "operation": "{x} + 6",
                "test": {"div": 19, True: 2, False: 0},
                "count": 0
            },
            2: {
                "items": [79, 60, 97],
                "operation": "{x} * {x}",
                "test": {"div": 13, True: 1, False: 3},
                "count": 0
            },
            3: {
                "items": [74],
                "operation": "{x} + 3",
                "test": {"div": 17, True: 0, False: 1},
                "count": 0
            }
        }
        for _ in range(20):
            monkey_business(monkeys)

        self.assertListEqual(monkeys[0]["items"], [10, 12, 14, 26, 34])
        self.assertListEqual(monkeys[1]["items"], [245, 93, 53, 199, 115])
        self.assertListEqual(monkeys[2]["items"], [])
        self.assertListEqual(monkeys[3]["items"], [])

        self.assertEqual(monkeys[0]["count"], 101)
        self.assertEqual(monkeys[1]["count"], 95)
        self.assertEqual(monkeys[2]["count"], 7)
        self.assertEqual(monkeys[3]["count"], 105)

    def test_part2(self):
        monkeys = {
            0: {
                "items": [79, 98],
                "operation": "{x} * 19",
                "test": {"div": 23, True: 2, False: 3},
                "count": 0
            },
            1: {
                "items": [54, 65, 75, 74],
                "operation": "{x} + 6",
                "test": {"div": 19, True: 2, False: 0},
                "count": 0
            },
            2: {
                "items": [79, 60, 97],
                "operation": "{x} * {x}",
                "test": {"div": 13, True: 1, False: 3},
                "count": 0
            },
            3: {
                "items": [74],
                "operation": "{x} + 3",
                "test": {"div": 17, True: 0, False: 1},
                "count": 0
            }
        }
        for _ in range(20):
            monkey_business(monkeys, high_stress=True)

        self.assertEqual(monkeys[0]["count"], 99)
        self.assertEqual(monkeys[1]["count"], 97)
        self.assertEqual(monkeys[2]["count"], 8)
        self.assertEqual(monkeys[3]["count"], 103)
