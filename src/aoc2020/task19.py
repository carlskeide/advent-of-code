# coding=utf-8
from ..utils import load_input

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
            a = resolve_rule(rules, "42")
            b = resolve_rule(rules, "31")
            # stdlib re doesn't support recursive regex ¯\_(ツ)_/¯
            return f"({a}{b}|{a*2}{b*2}|{a*3}{b*3}|{a*4}{b*4}|{a*5}{b*5})"

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
    ruledefs, messages = load_input(year=2020, day=19, group_lines=True)
    rules = {
        num: rule for num, rule in
        (r.split(": ") for r in ruledefs.splitlines())
    }

    matching = (valid_message(rules, msg) for msg in messages.splitlines())
    print(f"Part 1: {sum(matching)}")

    rules["8"] = "42 R"
    rules["11"] = "42 R 31"
    matching = (valid_message(rules, msg) for msg in messages.splitlines())
    print(f"Part 2: {sum(matching)}")
