from unittest import TestCase
import my_sort


class TestMySort(TestCase):
    def test_my_sort(self):
        self.assertEqual(my_sort.mySort([1, 2, 1]), [1, 1, 2])
        self.assertEqual(my_sort.mySort(['a', 'g', 'b']), ['a', 'b', 'g'])
        self.assertEqual(my_sort.mySort([120, 2, 1, 90, 100]), [1, 2, 90, 100, 120])
        self.assertEqual(my_sort.mySort([1, 2, 1, 3, 11, 1]), [1, 1, 1, 2, 3, 11])
        self.assertEqual(my_sort.mySort([1, 200, 1]), [1, 1, 200])
        self.assertEqual(my_sort.mySort(['aa', 'got', 'cat', 'cot']), ['aa', 'cat', 'cot', 'got'])
        self.assertEqual(my_sort.mySort([11]), [11])
