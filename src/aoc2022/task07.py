# coding=utf-8
from ..utils import load_input


def parse_output(output):
    fs = {}
    path = []
    pwd = fs
    for atoms in (line.split() for line in output):
        if atoms[0] == "$" and atoms[1] == "cd":
            dest = atoms[2]

            if dest == "..":
                path.pop()
                pwd = path[-1]

            else:
                if dest not in pwd:
                    pwd[dest] = {}

                pwd = pwd[dest]
                path.append(pwd)

        elif atoms[0] == "dir" and atoms[1] not in pwd:
            pwd[atoms[1]] = {}

        elif atoms[0].isnumeric():
            size, name = atoms
            pwd[name] = int(size)

    return fs


def find_directories(fs):
    for node in fs.values():
        if isinstance(node, dict):
            yield node
            yield from find_directories(node)


def rsize(fs):
    total = 0
    for node in fs.values():
        if isinstance(node, dict):
            total += rsize(node)
        else:
            total += node

    return total


if __name__ == "__main__":
    task_input = load_input(year=2022, day=7, group_lines=False)
    fs = parse_output(task_input)
    dir_sizes = [rsize(d) for d in find_directories(fs)]
    print(f"Part 1: {sum(size for size in dir_sizes if size <=100000)}")

    free_space = 70000000 - rsize(fs['/'])
    required = 30000000 - free_space

    for size in sorted(dir_sizes):
        if size > required:
            print(f"Part 2: {size}")
            break
