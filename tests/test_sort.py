import unittest
from algorithms.sort import Sorting, SortType


class TestSort(unittest.TestCase):
    """
    Create class instance
    """
    def setUp(self):
        self.sorting = Sorting([1, 11, 98, 3, 50, 72, 22, 29, 99, 2])

    def test_bubble_sort(self):
        self.assertEqual(self.sorting.bubble_sort(), [1, 2, 3, 11, 22, 29, 50, 72, 98, 99])

    def test_selection_sort(self):
        self.assertEqual(self.sorting.selection_sort(), [1, 2, 3, 11, 22, 29, 50, 72, 98, 99])
        self.assertEqual(self.sorting.selection_sort(sort_type=SortType.DESC), [99, 98, 72, 50, 29, 22, 11, 3, 2, 1])

    def test_selection(self):
        self.assertEqual(self.sorting.selection(1), 1)
        self.assertEqual(self.sorting.selection(2), 2)
        self.assertEqual(self.sorting.selection(3), 3)
        self.assertEqual(self.sorting.selection(4), 11)
        self.assertEqual(self.sorting.selection(5), 22)

        self.assertEqual(self.sorting.selection(1, sort_type=SortType.DESC), 99)
        self.assertEqual(self.sorting.selection(2, sort_type=SortType.DESC), 98)
        self.assertEqual(self.sorting.selection(3, sort_type=SortType.DESC), 72)

    def test_merge_sort(self):
        self.sorting.merge_sort()
        self.assertEqual(self.sorting.numbers, [1, 2, 3, 11, 22, 29, 50, 72, 98, 99])
