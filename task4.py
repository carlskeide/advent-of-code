#!/usr/bin/env python3
# coding=utf-8

# The expected fields are as follows:
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) [optional]


def validate(passport):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all((f"{field}:" in passport) for field in required)


if __name__ == "__main__":
    with open("./task4.input") as f:
        passports = f.read().split("\n\n")

    validation = [validate(passport) for passport in passports]
    print(f"Part 1: Valid passwords {sum(validation)} of {len(validation)}")
