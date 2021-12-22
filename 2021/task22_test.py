# coding=utf-8
from unittest import TestCase

from .task22 import *


class TestTask(TestCase):
    def test_parse_instruction(self):
        self.assertEqual(
            parse_instruction("off x=-10..5,y=17..27,z=-4..12"),
            ("off", (-10, 17, -4), (5, 27, 12)))

    def test_part1(self):
        reactor = Reactor()

        operations = [
            parse_instruction(s) for s in [
                "on x=-20..26,y=-36..17,z=-47..7",
                "on x=-20..33,y=-21..23,z=-26..28",
                "on x=-22..28,y=-29..23,z=-38..16",
                "on x=-46..7,y=-6..46,z=-50..-1",
                "on x=-49..1,y=-3..46,z=-24..28",
                "on x=2..47,y=-22..22,z=-23..27",
                "on x=-27..23,y=-28..26,z=-21..29",
                "on x=-39..5,y=-6..47,z=-3..44",
                "on x=-30..21,y=-8..43,z=-13..34",
                "on x=-22..26,y=-27..20,z=-29..19",
                "off x=-48..-32,y=26..41,z=-47..-37",
                "on x=-12..35,y=6..50,z=-50..-2",
                "off x=-48..-32,y=-32..-16,z=-15..-5",
                "on x=-18..26,y=-33..15,z=-7..46",
                "off x=-40..-22,y=-38..-28,z=23..41",
                "on x=-16..35,y=-41..10,z=-47..6",
                "off x=-32..-23,y=11..30,z=-14..3",
                "on x=-49..-5,y=-3..45,z=-29..18",
                "off x=18..30,y=-20..-8,z=-3..13",
                "on x=-41..9,y=-7..43,z=-33..15"
            ]
        ]
        for state, slice_min, slice_max in operations:
            reactor.toggle(slice_min, slice_max, state)

        self.assertEqual(sum(reactor.values()), 590784)
