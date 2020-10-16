from unittest import TestCase
import reverse_list


class TestReverseList(TestCase):
    def test_reverseShallow(self):
        self.assertEqual(reverse_list.reverseShallow([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list.reverseShallow([1]), [1])
        self.assertEqual(reverse_list.reverseShallow(['a', 'b', 'c']), ['c', 'b', 'a'])
        self.assertEqual(reverse_list.reverseShallow([0, 1, 2, 3]), [3, 2, 1, 0])
        self.assertEqual(reverse_list.reverseShallow([1, [2, 3]]), [[2, 3], 1])
        self.assertEqual(reverse_list.reverseShallow([1, 2, 3]), [3, 2, 1])

    def test_reverseDeep(self):
        self.assertEqual(reverse_list.reverseDeep([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list.reverseDeep([1]), [1])
        self.assertEqual(reverse_list.reverseDeep(['a', 'b', 'c']), ['c', 'b', 'a'])
        self.assertEqual(reverse_list.reverseDeep([0, 1, 2, 3]), [3, 2, 1, 0])
        self.assertEqual(reverse_list.reverseDeep([[0, 1, 2]]), [[2, 1, 0]])
        self.assertEqual(reverse_list.reverseDeep([1, [2, 3]]), [[3, 2], 1])
        self.assertEqual(reverse_list.reverseDeep([[1, 2], 3]), [3, [2, 1]])

