import unittest
from algorithms import compare_the_triplets


class TestCompareTheTriplets(unittest.TestCase):

    def test_solve(self):
        result = compare_the_triplets.solve(5, 6, 7, 3, 6, 10)
        self.assertEquals(result, '1 1')
