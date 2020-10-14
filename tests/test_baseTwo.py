from unittest import TestCase
import base_two


class TestBaseTwo(TestCase):
    def test_convertBase(self):
        self.assertEqual(base_two.convertBase(10), 1010)
        self.assertEqual(base_two.convertBase(1), 1)
        self.assertEqual(base_two.convertBase(0), 0)
        self.assertEqual(base_two.convertBase(2), 10)
        self.assertEqual(base_two.convertBase(3), 11)
        self.assertEqual(base_two.convertBase(11), 1011)
        self.assertEqual(base_two.convertBase(100), 1100100)
        self.assertEqual(base_two.convertBase(8), 1000)
        self.assertEqual(base_two.convertBase(4), 100)
