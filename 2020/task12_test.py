# coding=utf-8
from unittest import TestCase

from src.task12 import Navigator, WaypointNavigator


class TestNavigator(TestCase):
    navigator_class = Navigator

    instructions = [
        "F10",
        "N3",
        "F7",
        "R90",
        "F11"
    ]

    def setUp(self):
        self.navigator = self.navigator_class(face="E")

    def test_navigate(self):
        self.navigator.follow(self.instructions)

        self.assertEqual(self.navigator.face, "S")
        self.assertEqual(self.navigator.position, {"x": 17, "y": -8})
        self.assertEqual(self.navigator.distance, 25)


class TestWaypointNavigator(TestNavigator):
    navigator_class = WaypointNavigator

    def test_navigate(self):
        self.navigator.follow(self.instructions)

        self.assertEqual(self.navigator.position, {"x": 214, "y": -72})
        self.assertEqual(self.navigator.distance, 286)
