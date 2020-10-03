#!/usr/bin/python3

import unittest
import match_brackets


class TestMatchBrackets(unittest.TestCase):
    def test_matchBrackets(self):
        self.assertEqual(match_brackets.matchBrackets('(asdf)'), True)
        self.assertEqual(match_brackets.matchBrackets('(asdf))'), False)
        self.assertEqual(match_brackets.matchBrackets('({[]})'), True)
        self.assertEqual(match_brackets.matchBrackets('(((()'), False)
        self.assertEqual(match_brackets.matchBrackets('())))))'), False)
        self.assertEqual(match_brackets.matchBrackets('(asdf)'), True)
        self.assertEqual(match_brackets.matchBrackets('<a+{b * 2}>'), True)
        self.assertEqual(match_brackets.matchBrackets(''), True)
