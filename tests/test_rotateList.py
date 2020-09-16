#!/usr/bin/python3

import unittest
import rotate_list


class TestRotateList(unittest.TestCase):
    def test_rotateList(self):
        self.assertEqual(rotate_list.rotate([1, 2, 3], 1), [2, 3, 1])
        self.assertEqual(rotate_list.rotate([1, 2, 3], -1), [3, 1, 2])
        self.assertEqual(rotate_list.rotate(['a', 'b', 'c'], 2), ['c', 'a', 'b'])
