# coding=utf-8
from unittest import TestCase

from .task16 import *


class TestTask(TestCase):
    def test_parse_packet(self):
        self.assertDictEqual(
            list(parse_packet("110100101111111000101000"))[1],
            {"version": 6, "type": 4, "value": 2021}
        )

        self.assertDictEqual(
            list(parse_packet(
                "00111000000000000110111101000101001010010001001000000000"
            ))[1],
            {
                "version": 1,
                "type": 6,
                "value": [
                    {"version": 6, "type": 4, "value": 10},
                    {"version": 2, "type": 4, "value": 20}
                ]
            }
        )

        self.assertDictEqual(
            list(parse_packet(
                "11101110000000001101010000001100100000100011000001100000"
            ))[1],
            {
                "version": 7,
                "type": 3,
                "value": [
                    {"version": 2, "type": 4, "value": 1},
                    {"version": 4, "type": 4, "value": 2},
                    {"version": 1, "type": 4, "value": 3}
                ]
            }
        )
