# coding=utf-8
from unittest import TestCase

from .task06 import distinct_answers, common_answers


class TestTask(TestCase):
    answers = "abcx\nabcy\nabcz"
    answer_groups = [
        "abc",
        "a\nb\nc",
        "ab\nac",
        "a\na\na\na",
        "b"
    ]

    def test_distinct_answers(self):
        assert distinct_answers(self.answers) == set("abcxyz")

        result = list(map(distinct_answers, self.answer_groups))
        assert sum(len(x) for x in result) == 11

    def test_common_answers(self):
        result = list(map(common_answers, self.answer_groups))
        assert sum(len(x) for x in result) == 6
