# coding=utf-8
from unittest import TestCase

from .task02 import policy_num_letter, policy_letter_pos


class TestTask(TestCase):
    def test_policy1(self):
        self.assertTrue(policy_num_letter("1-3 a", "abcde"))
        self.assertFalse(policy_num_letter("1-3 b", "cdefg"))
        self.assertTrue(policy_num_letter("2-9 c", "ccccccccc"))

    def test_policy2(self):
        self.assertTrue(policy_letter_pos("1-3 a", "abcde"))
        self.assertFalse(policy_letter_pos("1-3 b", "cdefg"))
        self.assertFalse(policy_letter_pos("2-9 c", "ccccccccc"))
