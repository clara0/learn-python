import unittest
import possible_combinations


class TestPossibleCombos(unittest.TestCase):
    def test_findAll(self):
        self.assertEqual(possible_combinations.findAll(('a',), ('1',)), {'1a', 'a1'})
        self.assertEqual(possible_combinations.findAll(('a', 'b'), ('1',)), {'1b', 'b1', '1a', 'a1'})
