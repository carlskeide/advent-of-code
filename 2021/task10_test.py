# coding=utf-8
from unittest import TestCase

from .task10 import *


class TestTask(TestCase):
    def test_parse(self):
        self.assertEqual(
            list(parse("<{([{{}}[<[[[<>{}]]]>[]]")), ["]", ")", "}", ">"])

        self.assertRaises(ValueError, parse, "{([(<{}[<>[]}>{[]{[(<()>")
        self.assertRaises(ValueError, parse, "[[<[([]))<([[{}[[()]]]")
        self.assertRaises(ValueError, parse, "[{[{({}]{}}([{[{{{}}([]")
        self.assertRaises(ValueError, parse, "<{([([[(<>()){}]>(<<{{")

    def test_score_corruption(self):
        self.assertEqual(score_corruption("<{([{{}}[<[[[<>{}]]]>[]]"), 0)
        self.assertEqual(score_corruption("[{[{({}]{}}([{[{{{}}([]"), 57)

    def test_score_fill(self):
        self.assertEqual(score_fill("[{[{({}]{}}([{[{{{}}([]"), 0)
        self.assertEqual(score_fill("<{([{{}}[<[[[<>{}]]]>[]]"), 294)
