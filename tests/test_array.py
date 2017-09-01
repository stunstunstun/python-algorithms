import unittest
from algorithms.array import Array


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

    def test_reference(self):
        numbers = [98, 3, 50, 72, 22, 29, 99, 2, 1, 11]
        Array.pop(numbers)
        self.assertEqual(numbers, [98, 3, 50, 72, 22, 29, 99, 2, 1])

    def tearDown(self):
        """
        Print array elements
        """
        print('length = {}, elements = {}'.format(self.array.__len__(), self.array))
