# coding=utf-8
from . import load_input

from collections import defaultdict, Counter


class Cave:
    def __init__(self, charter):
        self.nodes = defaultdict(set)
        for a, b in (s.split('-') for s in charter):
            self.nodes[a].add(b)
            self.nodes[b].add(a)

    def find_paths(self):
        paths = []
        self.spelunk("start", [], paths)
        return paths

    def valid_path(self, trail, node):
        return (node != "start" and not (node.islower() and node in trail))

    def spelunk(self, node, trail, paths):
        path = trail + [node]
        for conn in self.nodes[node]:
            if conn == "end":
                # print(f"found path {'-'.join(trail)} -> {conn}")
                paths.append(path + ["end"])

            elif self.valid_path(trail, conn):
                self.spelunk(conn, path, paths)


if __name__ == "__main__":
    task_input = load_input(day=12, group_lines=False)

    paths = Cave(task_input).find_paths()
    print(f"Part 1: {len(paths)}")

    paths = ""
    print(f"Part 2: {len(paths)}")
