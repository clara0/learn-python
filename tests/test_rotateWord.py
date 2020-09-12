import unittest
import rotate_word


class TestRotateWord(unittest.TestCase):
    def test_rotateWord(self):
        self.assertEqual(rotate_word.rotate('abc', 1), 'bcd')
        self.assertEqual(rotate_word.rotate('abcz', 2), 'cdeb')
        self.assertEqual(rotate_word.rotate('abc', 27), 'bcd')
        self.assertEqual(rotate_word.rotate('abc', -1), 'zab')
        self.assertEqual(rotate_word.rotate('ABC', 1), 'bcd')
