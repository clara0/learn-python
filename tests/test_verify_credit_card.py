#!/usr/bin/python3

import unittest
import verify_credit_card


class TestVerifyCreditCard(unittest.TestCase):
    def listDigits0(self, function):
        self.assertEqual(function(123), (1, 2, 3))
        self.assertEqual(function(1), (1,))
        self.assertEqual(function(0), (0,))
        self.assertEqual(function(-123), (1, 2, 3))
        self.assertEqual(function(-1), (1,))
        self.assertEqual(function(-140), (1, 4, 0))
        self.assertEqual(function(123000000), (1, 2, 3, 0, 0, 0, 0, 0, 0))
        self.assertEqual(function(-123000000), (1, 2, 3, 0, 0, 0, 0, 0, 0))

    def test_listDigits(self):
        self.listDigits0(verify_credit_card.listDigits)

    def test_listDigits2(self):
        self.listDigits0(verify_credit_card.listDigits2)

    def test_LuhnTest(self):
        self.assertEqual(verify_credit_card.LuhnTest('4111111111111111'), True)
        self.assertEqual(verify_credit_card.LuhnTest('4111111111111112'), False)
        self.assertEqual(verify_credit_card.LuhnTest('49927398716'), True)
        self.assertEqual(verify_credit_card.LuhnTest('49927398717'), False)
        self.assertEqual(verify_credit_card.LuhnTest('1234567812345670'), True)
        self.assertEqual(verify_credit_card.LuhnTest('1234567812345671'), False)
