# coding=utf-8
from . import load_input

import re


def valid_message(rules, message):
    pattern = "^" + resolve_rule(rules, rules["0"]) + "$"
    return bool(re.match(pattern, message))


def resolve_rule(rules, rule):
    if '"' in rule:
        return rule.strip('"')

    elif "|" in rule:
        spec = "|".join(resolve_rule(rules, _or) for _or in rule.split(" | "))
        return f"({spec})"

    elif " " in rule:
        spec = "".join(resolve_rule(rules, _and) for _and in rule.split(" "))
        return f"({spec})"

    else:
        return resolve_rule(rules, rules[rule])


if __name__ == "__main__":
    ruledefs, messages = load_input(day=19, group_lines=True)
    rules = {
        num: rule for num, rule in
        (r.split(": ") for r in ruledefs.splitlines())
    }

    matching = (valid_message(rules, msg) for msg in messages.splitlines())
    print(f"Part 1: {sum(matching)}")

    part2 = ""
    print(f"Part 2: {part2}")
