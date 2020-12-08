# coding=utf-8
from utils import load_input


def decode(boarding_pass):
    rows = list(range(128))
    cols = list(range(8))

    for code in boarding_pass[:7]:
        half = len(rows) // 2
        rows = rows[:half] if code == "F" else rows[half:]

    for code in boarding_pass[7:]:
        half = len(cols) // 2
        cols = cols[:half] if code == "L" else cols[half:]

    return (rows[0], cols[0])


def seat_id(row, col):
    return row * 8 + col


def free_seat_ids(occupied):
    all_seats = ((row, col) for row in range(128) for col in range(8))
    return (seat_id(*seat) for seat in all_seats if seat not in occupied)


if __name__ == "__main__":
    occupied = [decode(line.strip()) for line in load_input(day=5)]

    occupied_ids = [seat_id(row, col) for row, col in occupied]
    print(f"Part 1: {max(occupied_ids)}")

    for free_id in free_seat_ids(occupied):
        if free_id - 1 in occupied_ids and free_id + 1 in occupied_ids:
            break

    else:
        raise ValueError("Didn't find a free seat")

    print(f"Part 2: {free_id}")
