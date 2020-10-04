#!/usr/bin/python3

import unittest
import factorial


class TestFactorial(unittest.TestCase):
    def findFactorial0(self, function):
        self.assertEqual(function(1), 1)
        self.assertEqual(function(4), 24)
        self.assertEqual(function(12), 479001600)

    def test_findFactorial(self):
        self.findFactorial0(factorial.findFactorial)

    def test_findFactorial2(self):
        self.findFactorial0(factorial.findFactorial2)