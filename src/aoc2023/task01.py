# coding=utf-8
from ..utils import load_input

# If it's stupid, but it works...
textual_numbers = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def calibration_value(text: str, textual=False) -> int:
    if textual:
        for sym, val in textual_numbers.items():
            text = text.replace(sym, val)

    nums = [s for s in text if s.isnumeric()]
    return int(nums[0] + nums[-1])


if __name__ == "__main__":
    task_input = load_input(year=2023, day=1, group_lines=False)

    part1 = sum(map(calibration_value, task_input))
    print(f"Part 1: {part1}")

    part2 = sum(calibration_value(line, textual=True) for line in task_input)
    print(f"Part 2: {part2}")
