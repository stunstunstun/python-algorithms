import unittest
from algorithms.dp import DP


class TestDP(unittest.TestCase):

    def test_fibonacci(self):
        dp = DP(100)
        self.assertEquals(dp.fibonacci(0), 0)
        self.assertEquals(dp.fibonacci(1), 1)
        self.assertEquals(dp.fibonacci(2), 1)
        self.assertEquals(dp.fibonacci(3), 2)
        self.assertEquals(dp.fibonacci(4), 3)
        self.assertEquals(dp.fibonacci(5), 5)
        self.assertEquals(dp.fibonacci(6), 8)
        self.assertEquals(dp.fibonacci(7), 13)
        self.assertEquals(dp.fibonacci(8), 21)
        self.assertEquals(dp.fibonacci(9), 34)
        self.assertEquals(dp.fibonacci(31), 1346269)
        self.assertEquals(dp.fibonacci(40), 102334155)
