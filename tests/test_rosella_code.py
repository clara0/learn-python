#!usr/bin/python3

import unittest
import rosella_code


class TestRosellaCode(unittest.TestCase):
    def test_rosellaCode(self):
        self.assertEqual(rosella_code.rosellaCode("test", "testing"), "test")
        self.assertEqual(rosella_code.rosellaCode("thisisatest", "123"), "")
        self.assertEqual(rosella_code.rosellaCode("onetwothree", "testing"), "te")
        self.assertEqual(rosella_code.rosellaCode("test", "testing"), "test")
