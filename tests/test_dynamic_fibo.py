import unittest
from algorithms.dynamic_fibo import DynamicFibo


class TestDynamicFibo(unittest.TestCase):

    def test_dynamic_fibo(self):
        fibo = DynamicFibo(100)

        self.assertEquals(fibo.value(0), 0)
        self.assertEquals(fibo.value(1), 1)
        self.assertEquals(fibo.value(2), 1)
        self.assertEquals(fibo.value(3), 2)
        self.assertEquals(fibo.value(4), 3)
        self.assertEquals(fibo.value(5), 5)
        self.assertEquals(fibo.value(6), 8)
        self.assertEquals(fibo.value(7), 13)
        self.assertEquals(fibo.value(8), 21)
        self.assertEquals(fibo.value(9), 34)
        self.assertEquals(fibo.value(31), 1346269)
