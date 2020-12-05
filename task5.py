#!/usr/bin/env python3
# coding=utf-8

# The first 7 characters will either be F or B; these specify exactly one of
# the 128 rows on the plane (numbered 0 through 127). Each letter tells you
# which half of a region the given seat is in. Start with the whole list of rows;
# the first letter indicates whether the seat is in the front (0 through 63)
# or the back (64 through 127). The next letter indicates which half of that
# region the seat is in, and so on until you're left with exactly one row.
# The last three characters will be either L or R; these specify exactly one
# of the 8 columns of seats on the plane (numbered 0 through 7). The same
# process as above proceeds again, this time with only three steps. L means
# to keep the lower half, while R means to keep the upper half.


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
    with open("./task5.input") as f:
        occupied = [decode(line.strip()) for line in f.readlines() if line]

    occupied_ids = [seat_id(row, col) for row, col in occupied]
    print(f"Part 1: {max(occupied_ids)}")

    for free_id in free_seat_ids(occupied):
        if free_id - 1 in occupied_ids and free_id + 1 in occupied_ids:
            break

    else:
        raise ValueError("Didn't find a free seat")

    print(f"Part 2: {free_id}")
