# coding=utf-8
import re
from .utils import load_input
from .models import SparseGrid


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


def find_trajectories(target, x_iter, y_iter):
    x_min, x_max, y_min, y_max = target
    for x_delta in x_iter:
        for y_delta in y_iter:
            trajectory = []
            for x, y in launch_probe(x_delta, y_delta):
                trajectory.append((x, y))
                if x_min <= x <= x_max and y_min >= y >= y_max:
                    # print(f"{(x_delta, y_delta)} Hit!")
                    yield ((x_delta, y_delta), trajectory)
                    break

                elif x > x_max or y < y_max:
                    # print(f"{(x_delta, y_delta)} Miss!")
                    break


def max_height(target):
    trajectories = find_trajectories(target, range(1, 50), range(1, 500))
    return max(max(y for _, y in trajectory) for _, trajectory in trajectories)


def distinct_deltas(target):
    trajectories = find_trajectories(target, range(1, 255), range(-255, 255))
    return sum(1 for _ in trajectories)


if __name__ == "__main__":
    target_spec, *_ = load_input(day=17, group_lines=False)
    target = parse_target(target_spec)

    part1 = max_height(target)
    print(f"Part 1: {part1}")

    part2 = distinct_deltas(target)
    print(f"Part 2: {part2}")
