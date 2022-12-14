# coding=utf-8
from ..utils import load_input


def parse_monkey(text):
    return {
        "id": int(text[0].split()[-1][:-1]),
        "items": list(eval(text[1].split(': ')[-1] + ",")),
        "operation": str.replace(text[2].split('= ')[-1], "old", "{x}"),
        "test": {
            "div": int(text[3].split()[-1]),
            True: int(text[4].split()[-1]),
            False: int(text[5].split()[-1]),
        },
        "count": 0
    }


def monkey_business(monkeys, high_stress=False):
    for monkey_id in sorted(monkeys.keys()):
        monkey = monkeys[monkey_id]
        while monkey["items"]:
            monkey["count"] += 1

            item = monkey["items"].pop(0)
            item = eval(monkey["operation"].format(x=item))
            if not high_stress:
                item //= 3

            target = monkey["test"][item % monkey["test"]["div"] == 0]
            monkeys[target]["items"].append(item)


if __name__ == "__main__":
    monkey_texts = load_input(year=2022, day=11, group_lines=True)
    monkeys = {}
    for text in monkey_texts:
        monkey = parse_monkey(text.splitlines())
        monkey_id = monkey.pop("id")
        monkeys[monkey_id] = monkey

    for _ in range(20):
        monkey_business(monkeys)

    top_monkeys = sorted(monkey["count"] for monkey in monkeys.values())
    print(f"Part 1: {top_monkeys[-1] * top_monkeys[-2]}")
