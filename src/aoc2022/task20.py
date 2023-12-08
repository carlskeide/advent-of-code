# coding=utf-8
from ..utils import load_input
from ..models import LinkedNode


def build_list(seed: list[int], rounds: int) -> LinkedNode:
    nodes = [LinkedNode(val) for val in seed]
    prev = nodes[-1]
    for node in nodes:
        prev.append(node)
        prev = node

    for _ in range(rounds):
        mix(nodes)

    return node.find(0)


def mix(nodes: list[LinkedNode]) -> None:
    length = len(nodes)
    for node in nodes:
        insert_node = node.remove().seek(node.val % (length - 1)).splice(node)


if __name__ == "__main__":
    task_input = [int(line) for line in load_input(year=2022, day=20)]

    zero = build_list(task_input, rounds=1)
    part1 = sum(zero.seek(n).val for n in (1000, 2000, 3000))
    print(f"Part 1: {part1}")

    part2_input = [i * 811589153 for i in task_input]
    zero = build_list(part2_input, rounds=10)
    part2 = sum(zero.seek(n).val for n in (1000, 2000, 3000))
    print(f"Part 2: {part2}")
