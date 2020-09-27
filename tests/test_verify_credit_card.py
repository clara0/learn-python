#!/usr/bin/python3

import unittest
import verify_credit_card


class TestVerifyCreditCard(unittest.TestCase):
    def test_listDigits(self):
        self.assertEqual(verify_credit_card.listDigits(123), (1, 2, 3))
        self.assertEqual(verify_credit_card.listDigits(1), (1,))

    def test_LuhnTest(self):
        self.assertEqual(verify_credit_card.LuhnTest('4111111111111111'), True)
        self.assertEqual(verify_credit_card.LuhnTest('4111111111111112'), False)
        self.assertEqual(verify_credit_card.LuhnTest('49927398716'), True)
        self.assertEqual(verify_credit_card.LuhnTest('49927398717'), False)
        self.assertEqual(verify_credit_card.LuhnTest('1234567812345670'), True)
        self.assertEqual(verify_credit_card.LuhnTest('1234567812345671'), False)
