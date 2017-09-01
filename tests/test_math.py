import unittest
from algorithms.math import Math


class TestMath(unittest.TestCase):

    def test_format(self):
        self.assertEqual(Math.bin(10), '1010')
        self.assertEqual(Math.bin(255), '11111111')
        self.assertEqual(Math.oct(10), '12')
        self.assertEqual(Math.oct(255), '377')

    def test_prime(self):
        self.assertEqual(Math.prime(0), False)
        self.assertEqual(Math.prime(1), False)
        self.assertEqual(Math.prime(2), True)
        self.assertEqual(Math.prime(3), True)
        self.assertEqual(Math.prime(4), False)
        self.assertEqual(Math.prime(5), True)
        self.assertEqual(Math.prime(13), True)
        self.assertEqual(Math.prime(1000000007), True)
        self.assertEqual(Math.prime(1000003), True)
