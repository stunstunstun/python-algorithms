import unittest

from algorithms import Array


class TestArray(unittest.TestCase):
    """
    Create class instance
    """
    def setUp(self):
        self.array = Array('1 2 3 4 10 11')
    """
    Test that the result sum of all numbers
    """
    def test_sum(self):
        result = self.array.sum(6)
        self.assertEqual(result, 31)
    """
    Tests that an exception occurs when the number of arguments is different
    """
    def test_sum_raise_exception(self):
        self.assertRaises(Exception, lambda: self.array.sum(5))
    """
    Print array elements
    """
    def tearDown(self):
        print('length = {}, elements = {}'.format(self.array.__len__(), self.array))
