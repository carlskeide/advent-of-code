# coding=utf-8
from ..utils import load_input

import re
import math


def parse_rules(rule_specs):
    rule_dict = {}
    for rule in rule_specs:
        parsed = re.match(r"^([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)$", rule)
        rule_name, p1, p2, p3, p4 = parsed.groups()
        rule_dict[rule_name] = [(int(p1), int(p2)), (int(p3), int(p4))]

    return rule_dict


def invalid_fields(rules, ticket):
    fields = map(int, ticket.split(','))
    invalid = False
    for field in fields:
        for r1, r2 in rules.values():
            if (r1[0] <= field <= r1[1]) or (r2[0] <= field <= r2[1]):
                break

        else:
            invalid += field

    return invalid


def match_rules(rules, valid_tickets):
    tickets = [tuple(map(int, ticket.split(","))) for ticket in valid_tickets]
    num_fields = len(tickets[0])
    rule_map = {}
    for rule_name, rule in rules.items():
        rule_map[rule_name] = []

        for i in range(num_fields):
            for ticket in tickets:
                if not (
                    (rule[0][0] <= ticket[i] <= rule[0][1])
                    or (rule[1][0] <= ticket[i] <= rule[1][1])
                ):
                    break

            else:
                rule_map[rule_name].append(i)

    ticket_fields = {}
    match_fields = list(range(num_fields))
    while match_fields:
        for i in match_fields:
            for rule_name, fields in rule_map.items():
                if [f for f in fields if f in match_fields] == [i]:
                    ticket_fields[rule_name] = i
                    match_fields.pop(match_fields.index(i))
                    break

    return ticket_fields


if __name__ == "__main__":
    task_input = load_input(year=2020, day=16, group_lines=True)
    rules = parse_rules(task_input[0].splitlines())
    my_ticket = [int(f) for f in task_input[1].splitlines()[1].split(",")]
    tickets = task_input[2].splitlines()[1:]

    error_rate = sum(invalid_fields(rules, ticket) for ticket in tickets)
    print(f"Part 1: {error_rate}")

    valid_nearby = [ticket for ticket in tickets if not invalid_fields(rules, ticket)]
    ticket_fields = match_rules(rules, valid_nearby)
    departure_fields = (
        my_ticket[i] for rule, i in ticket_fields.items()
        if rule.startswith("departure")
    )
    print(f"Part 2: {math.prod(departure_fields)}")
