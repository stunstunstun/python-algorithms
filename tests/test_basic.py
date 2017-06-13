import unittest

from src.basic import (
    array
)


class TestArray(unittest.TestCase):
    def test_array_sum(self):
        output = array.Array.sum(6, [1, 2, 3, 4, 10, 11])
        self.assertEqual(output, 31)

    def test_array_sum_exception(self):
        self.assertRaises(Exception, lambda: array.Array.sum(5, [1, 2, 3, 4, 10, 11]))

    def test_array_sum_string(self):
        obj = array.Array()
        output = obj.sum(6, [1, 2, 3, 4, 10, 11])
        self.assertEqual(output, 31)

    def test_array_sum_string_exception(self):
        obj = array.Array()
        self.assertRaises(Exception, lambda: obj.sum(5, [1, 2, 3, 4, 10, 11]))
