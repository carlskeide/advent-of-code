# coding=utf-8
import operator
from functools import reduce

from ..utils import load_input


def parse_input(line: str) -> dict:
    game, draws = line.split(": ")
    parsed = {
        "id": int(game.split()[-1]),
        "draws": []
    }

    for draw in draws.split("; "):
        draw_dict = {}
        for group in draw.split(", "):
            count, color = group.split()
            draw_dict[color] = int(count)

        parsed["draws"].append(draw_dict)

    return parsed


def is_possible(draws: list[dict[str, int]], **target: int) -> bool:
    return all(
        count <= target[color]
        for draw in draws
        for color, count in draw.items()
    )


def min_cubes(draws: list[dict[str, int]]) -> dict[str, int]:
    cubes = {}
    for draw in draws:
        for color, count in draw.items():
            if count > cubes.get(color, 0):
                cubes[color] = count

    return cubes


if __name__ == "__main__":
    task_input = load_input(year=2023, day=2, group_lines=False)
    parsed_input = list(map(parse_input, task_input))

    part1 = sum(game["id"] for game in parsed_input
                if is_possible(game["draws"], red=12, green=13, blue=14))

    print(f"Part 1: {part1}")

    part2 = sum(
        reduce(operator.mul, (min_cubes(game["draws"]).values()))
        for game in parsed_input
    )
    print(f"Part 2: {part2}")
