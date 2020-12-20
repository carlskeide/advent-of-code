# coding=utf-8
from . import load_input

import re


def valid_message(rules, message):
    pattern = "^" + resolve_rule(rules, "0") + "$"
    return bool(re.match(pattern, message))


def resolve_rule(rules, rulenum):
    rule = rules[rulenum]

    if '"' in rule:
        return rule.strip('"')

    elif "R" in rule:
        if rulenum == "8":
            return resolve_rule(rules, "42") + "+"

        elif rulenum == "11":
            return resolve_rule(rules, "42") + "+" + resolve_rule(rules, "31") + "+"

    elif "|" in rule:
        ors = []
        for _or in rule.split(" | "):
            ands = []
            for _and in _or.split(" "):
                ands.append(resolve_rule(rules, _and))

            ors.append("".join(ands))

        spec = "|".join(ors)
        return f"({spec})"

    elif " " in rule:
        spec = "".join(resolve_rule(rules, _and) for _and in rule.split(" "))
        return f"({spec})"

    else:
        return resolve_rule(rules, rule)


if __name__ == "__main__":
    ruledefs, messages = load_input(day=19, group_lines=True)
    rules = {
        num: rule for num, rule in
        (r.split(": ") for r in ruledefs.splitlines())
    }

    matching = (valid_message(rules, msg) for msg in messages.splitlines())
    print(f"Part 1: {sum(matching)}")

    rules["8"] = "42 | 42 R"
    rules["11"] = "42 31 | 42 R 31"
    matching = (valid_message(rules, msg) for msg in messages.splitlines())
    print(f"Part 2: {sum(matching)}")
