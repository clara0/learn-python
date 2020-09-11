import unittest
import powers


class TestPowers(unittest.TestCase):
    def test_powers(self):
        result1 = powers.isPower(10, 100)
        self.assertEqual(result1, True)

        result2 = powers.isPower(11, 1331)
        self.assertEqual(result2, True)

        result3 = powers.isPower(2, 8)
        self.assertEqual(result3, True)

        result4 = powers.isPower(0, 100)
        self.assertEqual(result4, False)

        result5 = powers.isPower(1, 0)
        self.assertEqual(result5, False)

        result6 = powers.isPower('blah', 1)
        self.assertEqual(result6, False)
