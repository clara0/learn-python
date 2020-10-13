from unittest import TestCase
import check_phone_number


class TestCheckPhoneNumber(TestCase):
    def test_checkPhoneNum(self):
        self.assertTrue(check_phone_number.checkPhoneNum('555-555-5555'))
        self.assertTrue(check_phone_number.checkPhoneNum('(555)555-5555'))
        self.assertTrue(check_phone_number.checkPhoneNum('(555) 555-5555'))
        self.assertTrue(check_phone_number.checkPhoneNum('555 555 5555'))
        self.assertTrue(check_phone_number.checkPhoneNum('5555555555'))
        self.assertTrue(check_phone_number.checkPhoneNum('1 555-555-5555'))
        self.assertTrue(check_phone_number.checkPhoneNum('1(555) 555-5555'))
        self.assertTrue(check_phone_number.checkPhoneNum('1(555)555-5555'))
        self.assertTrue(check_phone_number.checkPhoneNum('1(555) 555 5555'))
        self.assertTrue(check_phone_number.checkPhoneNum('1 552 235 5490'))
        self.assertFalse(check_phone_number.checkPhoneNum('2(555) 555 5555'))
        self.assertFalse(check_phone_number.checkPhoneNum('1jjj 555 5555'))
        self.assertFalse(check_phone_number.checkPhoneNum('1 234234 555 5555'))
        self.assertFalse(check_phone_number.checkPhoneNum('2( 555 5555'))
        self.assertFalse(check_phone_number.checkPhoneNum('2555) 555 5555'))
        self.assertFalse(check_phone_number.checkPhoneNum('(1 (555 555 5555)'))
        self.assertFalse(check_phone_number.checkPhoneNum('(1 (555 dddddd55   5555)'))
