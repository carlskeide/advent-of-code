# coding=utf-8
from unittest import TestCase

from src.task18 import ltr_maths, parenthezise


class TestTask(TestCase):
    expr = [
        "1 + 2 * 3 + 4 * 5 + 6",
        "1 + (2 * 3) + (4 * (5 + 6))",
        "2 * 3 + (4 * 5)",
        "5 + (8 * 3 + 9 + 3 * 4 * 3)",
        "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
        "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
    ]

    def test_ltr_maths(self):
        self.assertEqual(ltr_maths(self.expr[0]), 71)
        self.assertEqual(ltr_maths(self.expr[1]), 51)
        self.assertEqual(ltr_maths(self.expr[2]), 26)
        self.assertEqual(ltr_maths(self.expr[3]), 437)
        self.assertEqual(ltr_maths(self.expr[4]), 12240)
        self.assertEqual(ltr_maths(self.expr[5]), 13632)

    def test_parenthezise(self):
        parenthezised = [parenthezise(e) for e in self.expr]
        self.assertEqual(ltr_maths(parenthezised[0]), 231)
        self.assertEqual(ltr_maths(parenthezised[1]), 51)
        self.assertEqual(ltr_maths(parenthezised[2]), 46)
        self.assertEqual(ltr_maths(parenthezised[3]), 1445)
        self.assertEqual(ltr_maths(parenthezised[4]), 669060)
        self.assertEqual(ltr_maths(parenthezised[5]), 23340)
