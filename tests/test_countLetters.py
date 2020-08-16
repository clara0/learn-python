import unittest
import os
import count_letters


class TestCountLetters(unittest.TestCase):
    def setUp(self):
        with open('/tmp/a.txt', 'w+') as fhand:
            fhand.write('aaabbc')

    def tearDown(self):
        os.remove('/tmp/a.txt')

    def test_countLetters(self):
        fhand = open('/tmp/a.txt')
        dictionary = count_letters.countLetters(fhand)
        print(dictionary)
        self.assertEqual(dictionary[0], ('c', 1))
        self.assertEqual(dictionary[1], ('b', 2))
        self.assertEqual(dictionary[2], ('a', 3))

