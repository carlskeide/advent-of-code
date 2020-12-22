# coding=utf-8
from . import load_input

import re
from collections import defaultdict
from functools import reduce
from pprint import pprint


def unsafe_ingredients(charter):
    allergens = defaultdict(list)

    for items, listed_allergens in charter:
        for allergen in listed_allergens:
            allergens[allergen].append(set(items))

    for allergen in allergens:
        allergens[allergen] = reduce(set.intersection, allergens[allergen])

    return allergens


if __name__ == "__main__":
    task_input = load_input(day=21)
    charter = []
    for line in task_input:
        things, allergens = re.match(r"^(.*) \(contains (.*)\)", line).groups()
        charter.append((things.split(), allergens.replace(',', '').split()))

    unsafe = unsafe_ingredients(charter)
    unsafe_items = reduce(set.union, unsafe.values())
    pprint(unsafe)
    ingredients = []
    for items, _ in charter:
        ingredients.extend(item for item in items if item not in unsafe_items)

    print(f"Part 1: {len(ingredients)}")

    matched = {}
    while len(matched) < len(unsafe):
        for allergen in unsafe:
            if len(unsafe[allergen]) == 1:
                match = unsafe[allergen].pop()
                matched[allergen] = match
                for other in unsafe:
                    if other != allergen and match in unsafe[other]:
                        unsafe[other] ^= {match, }

    print(f"Part 2: {','.join(matched[key] for key in sorted(matched))}")
