# coding=utf-8
from ..utils import load_input


def holiday_hash(string):
    current = 0
    for char in string:
        current = (current + ord(char)) * 17 % 256

    return current


def lens_map(steps: list[str]) -> dict[int, dict[str, int]]:
    boxes = {n: {} for n in range(256)}

    for step in steps:
        if step.endswith("-"):
            label = step[:-1]
            try:
                boxes[holiday_hash(label)].pop(label)
            except KeyError:
                pass

        elif "=" in step:
            label, focus = step.split("=")
            boxes[holiday_hash(label)][label] = int(focus)

    return boxes


def focus(boxes: dict[int, dict[str, int]]) -> int:
    val = 0
    for box, lenses in boxes.items():
        for slot, lens in enumerate(lenses.values(), start=1):
            val += (box + 1) * slot * lens

    return val

if __name__ == "__main__":
    task_input = load_input(year=2023, day=15, group_lines=False)
    init_seq = task_input[0].split(",")

    part1 = sum(map(holiday_hash, init_seq))
    print(f"Part 1: {part1}")

    part2 = focus(lens_map(init_seq))
    print(f"Part 2: {part2}")
