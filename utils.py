# coding=utf-8

def load_input(day, group_lines=False):
    with open(f"./task{day}.input", 'r') as f:
        content = f.read()

    return content.split("\n\n") if group_lines else content.splitlines()
