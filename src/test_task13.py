# coding=utf-8
from unittest import TestCase

from .task13 import next_bus, bus_contest


class TestBusSchedule(TestCase):
    def test_next_bus(self):
        timetable = [7, 13, 59, 31, 19]
        time, bus = next_bus(timetable, 939)

        self.assertEqual(time, 944)
        self.assertEqual(bus, 59)

    def test_bus_contest(self):
        time = bus_contest([17, None, 13, 19])
        self.assertEqual(time, 3417)

        time = bus_contest([67, 7, 59, 61])
        self.assertEqual(time, 754018)

        time = bus_contest([67, None, 7, 59, 61])
        self.assertEqual(time, 779210)

        time = bus_contest([7, 13, None, None, 59, None, 31, 19])
        self.assertEqual(time, 1068781)

        time = bus_contest([67, 7, None, 59, 61])
        self.assertEqual(time, 1261476)

        time = bus_contest([1789, 37, 47, 1889])
        self.assertEqual(time, 1202161486)
