import unittest
import powers


class TestPowers(unittest.TestCase):
    def test_powers(self):
        self.assertEqual(powers.isPower(10, 100), True)
        self.assertEqual(powers.isPower(11, 1331), True)
        self.assertEqual(powers.isPower(2, 8), True)
        self.assertEqual(powers.isPower(0, 100), False)
        self.assertEqual(powers.isPower(1, 0), False)
        self.assertEqual(powers.isPower('blah', 1), False)
