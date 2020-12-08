# coding=utf-8
from utils import load_input

import re

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
validators = {
    "byr": lambda x: (1920 <= int(x) <= 2002),
    "iyr": lambda x: (2010 <= int(x) <= 2020),
    "eyr": lambda x: (2020 <= int(x) <= 2030),
    "hcl": lambda x: re.match(r"^#[\da-f]{6}$", x),
    "pid": lambda x: re.match(r"^\d{9}$", x),
    "ecl": lambda x: re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", x),
    "hgt": lambda x: (
        (150 <= int(x.replace("cm", "")) <= 193)
        if "cm" in x else
        (59 <= int(x.replace("in", "")) <= 76)
    ),
    "cid": lambda x: True
}


def validate_fields(passport):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all((f"{field}:" in passport) for field in required)


def validate_strict(passport):
    fields = dict(s.split(":") for s in passport.split())
    try:
        return all(fn(fields.get(key, "")) for key, fn in validators.items())

    except ValueError:
        return False


if __name__ == "__main__":
    passports = load_input(day=4, group_lines=True)

    result = [validate_fields(passport) for passport in passports]
    print(f"Part 1: Valid passports {sum(result)} of {len(result)}")

    result = [validate_strict(passport) for passport in passports]
    print(f"Part 2: Strictly valid passports {sum(result)}")
