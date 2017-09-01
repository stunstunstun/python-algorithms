import unittest
from algorithms.search import Search


class TestSearch(unittest.TestCase):

    def test_binary_search_recursive(self):
        self.assertEqual(Search.binary_search([1, 2, 3, 11, 22, 29, 50, 72, 98, 99], 11), 3)

    def test_binary_search_iterative(self):
        self.assertEqual(Search.binary_search_iterative([1, 2, 3, 11, 22, 29, 50, 72, 98, 99], 11), 3)
        self.assertEqual(Search.binary_search_iterative([1, 2, 3, 4, 5], 3), 2)

    def test_ice_cream_parlor(self):
        self.assertEqual(Search.ice_cream_parlor(4, [1, 4, 5, 3, 2]), '1 4')
        self.assertEqual(Search.ice_cream_parlor(4, [2, 2, 4, 3]), '1 2')
