# coding=utf-8
import re
from .utils import load_input
# from .models import SparseGrid


def parse_target(description):
    matched = re.match(r"^.*x=(\d+)..(\d+), y=(\-?\d+)..(\-?\d+)", description)
    x_min, x_max, y_max, y_min = map(int, matched.groups())
    return x_min, x_max, y_min, y_max


def launch_probe(x_delta, y_delta):
    x = y = 0
    while True:
        x += x_delta
        y += y_delta

        yield (x, y)

        x_delta -= (x_delta > 0)
        y_delta -= 1


def max_height(target):
    x_min, x_max, y_min, y_max = target
    valid = []

    for x_delta in range(1,100):
        for y_delta in range(1,3000):
            # print(f"Launching with {(x_delta, y_delta)}", end=" ")

            trajectory = []
            for x, y in launch_probe(x_delta, y_delta):
                trajectory.append((x, y))
                if x_min <= x <= x_max and y_min >= y >= y_max:
                    print(f"{(x_delta, y_delta)} Hit! max_y: {max(y for _, y in trajectory)}")
                    valid.append(trajectory)
                    break

                elif x > x_max or y < y_max:
                    # print(f"Miss! {trajectory}")
                    break

    if not valid:
        raise Exception("No shots hit")

    return max(max(y for _, y in trajectory) for trajectory in valid)


if __name__ == "__main__":
    target_spec, *_ = load_input(day=17, group_lines=False)

    part1 = max_height(parse_target(target_spec))
    print(f"Part 1: {part1}")

    part2 = ""
    print(f"Part 2: {part2}")
