import unittest
from algorithms.array import Array, SortType


class TestArray(unittest.TestCase):
    """
    Create class instance
    """
    def setUp(self):
        self.array = Array('1 11 98 3 50 72 22 29 99 2')

    def test_sum(self):
        """
        Test that the result sum of all numbers
        """
        result = self.array.sum(10)
        self.assertEqual(result, 387)

    def test_sum_raise_exception(self):
        """
        Tests that an exception occurs when the number of arguments is different
        """
        self.assertRaises(Exception, lambda: self.array.sum(5))

    def test_rotate(self):
        self.assertEqual(self.array.rotate(2), [98, 3, 50, 72, 22, 29, 99, 2, 1, 11])

    def test_bubble_sort(self):
        self.assertEqual(self.array.bubble_sort(), [1, 2, 3, 11, 22, 29, 50, 72, 98, 99])

    def test_selection_sort(self):
        self.assertEqual(self.array.selection_sort(), [1, 2, 3, 11, 22, 29, 50, 72, 98, 99])
        self.assertEqual(self.array.selection_sort(sort_type=SortType.DESC), [99, 98, 72, 50, 29, 22, 11, 3, 2, 1])

    def test_selection(self):
        self.assertEqual(self.array.selection(1), 1)
        self.assertEqual(self.array.selection(2), 2)
        self.assertEqual(self.array.selection(3), 3)
        self.assertEqual(self.array.selection(4), 11)
        self.assertEqual(self.array.selection(5), 22)

        self.assertEqual(self.array.selection(1, sort_type=SortType.DESC), 99)
        self.assertEqual(self.array.selection(2, sort_type=SortType.DESC), 98)
        self.assertEqual(self.array.selection(3, sort_type=SortType.DESC), 72)

    def test_binary_search_recursive(self):
        self.array.bubble_sort()
        self.assertEqual(self.array.binary_search(11), 3)
        self.assertEqual(self.array.binary_search(11), 3)

    def test_binary_search_iterative(self):
        self.array.bubble_sort()
        self.assertEqual(Array.binary_search_iterative([1, 2, 3, 11, 22, 29, 50, 72, 98, 99], 11), 3)
        self.assertEqual(Array.binary_search_iterative([1, 2, 3, 4, 5], 3), 2)

    def test_ice_cream_parlor(self):
        self.assertEqual(Array.ice_cream_parlor(4, [1, 4, 5, 3, 2]), '1 4')
        self.assertEqual(Array.ice_cream_parlor(4, [2, 2, 4, 3]), '1 2')

    def tearDown(self):
        """
        Print array elements
        """
        print('length = {}, elements = {}'.format(self.array.__len__(), self.array))
