import unittest
import possible_combinations


class TestPossibleCombos(unittest.TestCase):
    def test_findAll(self):
        result = possible_combinations.findAll(('a',), ('1',))
        self.assertEqual(result, {'1a', 'a1'})
        result = possible_combinations.findAll(('a', 'b'), ('1',))
        self.assertEqual(result, {'1b', 'b1', '1a', 'a1'})
