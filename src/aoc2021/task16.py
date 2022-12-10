# coding=utf-8
import operator
from functools import reduce
from ..utils import load_input

OPCODES = {
    0: sum,
    1: lambda x: reduce(operator.mul, x),
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1]),
}

def parse_packet(packet):
    parsed = {
        "version": int(packet[0:3], 2),
        "type": int(packet[3:6], 2),
        "value": None
    }
    offset = 6

    if parsed["type"] == 4:
        value_string = ""

        while True:
            more = int(packet[offset])
            value_string += packet[offset + 1: offset + 5]
            offset += 5

            if not more:
                break

        parsed["value"] = int(value_string, 2)

    else:
        lentype = packet[offset]
        if lentype == "0":
            # next 15 bits == total length of children
            length = int(packet[offset + 1: offset + 16], 2)

            offset += 16

            parsed["value"] = []
            stop = offset + length
            while offset < stop:
                i, child = parse_packet(packet[offset:])
                parsed["value"].append(child)
                offset += i

        else:
            # next 11 bits == number of children
            num = int(packet[offset + 1: offset + 12], 2)
            offset += 12

            parsed["value"] = []
            for _ in range(num):
                i, child = parse_packet(packet[offset:])
                parsed["value"].append(child)
                offset += i

    return offset, parsed


def sum_versions(parsed):
    if parsed["type"] == 4:
        return parsed["version"]

    else:
        return (
            parsed["version"]
            + sum(sum_versions(child) for child in parsed["value"])
        )


def execute(obj):
    if obj["type"] == 4:
        return obj["value"]
    else:
        values = [execute(child) for child in obj["value"]]
        return OPCODES[obj["type"]](values)


if __name__ == "__main__":
    task_input = load_input(year=2021, day=16, group_lines=False)
    packet = bin(int(task_input[0], 16))[2:]

    _, parsed = parse_packet(packet)
    print(f"Part 1: {sum_versions(parsed)}")
    print(f"Part 2: {execute(parsed)}")
