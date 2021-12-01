# coding=utf-8
from . import load_input


def next_bus(timetable, current_time):
    while True:
        current_time += 1
        for bus in timetable:
            if current_time % bus == 0:
                return current_time, bus


def bus_contest(timetable):
    pattern = [(i, slot) for i, slot in enumerate(timetable) if slot]
    time = 0
    while True:
        time += timetable[0]
        for i, p in pattern:
            if (time + i) % p:
                break

        else:
            return time


if __name__ == "__main__":
    task_input = load_input(day=13)
    current_time = int(task_input[0])
    timetable = [
        (int(bus) if bus.isnumeric() else None)
        for bus in task_input[1].split(",")
    ]

    buses = [bus for bus in timetable if bus]
    time, bus = next_bus(buses, current_time)
    print(f"Part 1: {bus * (time - current_time)}")

    print(f"Part 2: {bus_contest(timetable)}")
