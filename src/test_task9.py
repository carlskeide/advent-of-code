# coding=utf-8
from unittest import TestCase

from .task9 import validate, validate_list, find_weakness


class TaskTests(TestCase):
    data = [
        35, 20, 15, 25, 47,
        40, 62, 55, 65, 95,
        102, 117, 150, 182,
        127, 219, 299, 277,
        309, 576
    ]

    def test_validator(self):
        data = list(range(1, 26))
        self.assertTrue(validate(data, 26))
        self.assertTrue(validate(data, 49))
        self.assertFalse(validate(data, 100))
        self.assertFalse(validate(data, 50))

        data.pop(data.index(20))
        data.append(45)

        self.assertTrue(validate(data, 26))
        self.assertFalse(validate(data, 65))
        self.assertTrue(validate(data, 64))
        self.assertTrue(validate(data, 66))

    def test_validate_list(self):
        with self.assertRaises(ValueError) as exc:
            validate_list(self.data, preamble=5)

        self.assertEqual(exc.exception.args[0], 127)

    def test_find_weakness(self):
        weakness = find_weakness(self.data, 127)
        self.assertListEqual(weakness, [15, 25, 47, 40])
