# coding=utf-8
from . import load_input

from collections import defaultdict


class Cave:
    def __init__(self, charter):
        self.nodes = defaultdict(set)
        for a, b in (s.split('-') for s in charter):
            self.nodes[a].add(b)
            self.nodes[b].add(a)

    def find_paths(self):
        return list(self.spelunk(trail=[], node="start"))

    def valid_path(self, trail, node):
        return (node != "start" and not (node.islower() and node in trail))

    def spelunk(self, trail, node):
        path = trail + [node]
        for next_node in self.nodes[node]:
            if next_node == "end":
                # print(f"found path {'-'.join(path)} -> {next_node}")
                yield path + [next_node]

            elif self.valid_path(path, next_node):
                yield from self.spelunk(path, next_node)


class DoubleDipCave(Cave):
    def valid_path(self, trail, node):
        if node == "start":
            return False

        elif node.islower() and node in trail:
            small_nodes = list(filter(str.islower, trail))
            return len(small_nodes) == len(set(small_nodes))

        else:
            return True


if __name__ == "__main__":
    task_input = load_input(day=12, group_lines=False)

    paths = Cave(task_input).find_paths()
    print(f"Part 1: {len(paths)}")

    paths = DoubleDipCave(task_input).find_paths()
    print(f"Part 2: {len(paths)}")
