# coding=utf-8
from unittest import TestCase

from .task18 import *


class TestTask(TestCase):
    def test_add(self):
        result = SnailFishNumber([[[[4,3],4],4],[7,[[8,4],9]]]) + SnailFishNumber([1,1])
        self.assertEqual(result.data, [[[[0,7],4],[[7,8],[6,0]]],[8,1]])

        result = reduce(add, map(SnailFishNumber, [[1,1], [2,2], [3,3], [4,4], [5,5], [6,6]]))
        self.assertEqual(result.data, [[[[5,0],[7,4]],[5,5]],[6,6]])

        result = reduce(add,
            map(SnailFishNumber, [
                [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
                [7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
                [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
                [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
                [7,[5,[[3,8],[1,4]]]],
                [[2,[2,2]],[8,[8,1]]],
                [2,9],
                [1,[[[9,3],9],[[9,0],[0,7]]]],
                [[[5,[7,4]],7],1],
                [[[[4,2],2],6],[8,7]]
            ])
        )
        self.assertEqual(result.data, [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])

    def test_get_magnitude(self):
        self.assertEqual(SnailFishNumber([9,1]).get_magnitude(), 29)
        self.assertEqual(SnailFishNumber([[[[3,0],[5,3]],[4,4]],[5,5]]).get_magnitude(), 791)
        self.assertEqual(SnailFishNumber([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]).get_magnitude(), 3488)
