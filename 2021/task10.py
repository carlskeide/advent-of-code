# coding=utf-8
from . import load_input

PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}

DEBUG_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETE_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}


def parse(line):
    stack = []
    for char in line:
        if char in PAIRS:
            stack.append(char)

        elif char == PAIRS[stack[-1]]:
            stack.pop()

        else:
            raise ValueError(char)

    return (PAIRS[c] for c in reversed(stack))


def score_corruption(line):
    try:
        parse(line)
        return 0

    except ValueError as e:
        return DEBUG_SCORE[str(e)]


def score_fill(line):
    try:
        completion = parse(line)

    except ValueError:
        return 0

    score = 0
    for char in completion:
        score *= 5
        score += COMPLETE_SCORE[char]

    return score


if __name__ == "__main__":
    task_input = load_input(day=10, group_lines=False)

    part1 = sum(score_corruption(line) for line in task_input)
    print(f"Part 1: {part1}")

    scores = list(filter(None, (score_fill(line) for line in task_input)))
    part2 = sorted(scores)[len(scores) // 2]
    print(f"Part 2: {part2}")
