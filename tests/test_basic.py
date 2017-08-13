import unittest
from algorithms.basic import Basic


class TestBasic(unittest.TestCase):

    def test_range_loop(self):
        # 1 2 3
        n = [1, 2]
        n.append(3)
        # 3 2 1
        n = list(reversed(n))
        self.assertEqual(n, [3, 2, 1])
        self.assertEqual(n, list(range(3, 0, -1)))
        # 1 3 5
        n = [1, 3, 5]
        self.assertEqual(n, list(range(1, 6, 2)))

    def test_factorial(self):
        self.assertEquals(Basic.factorial(5), 120)

    def test_fibonacci(self):
        self.assertEquals(Basic.fibonacci(0), 0)
        self.assertEquals(Basic.fibonacci(1), 1)
        self.assertEquals(Basic.fibonacci(2), 1)
        self.assertEquals(Basic.fibonacci(3), 2)
        self.assertEquals(Basic.fibonacci(4), 3)
        self.assertEquals(Basic.fibonacci(5), 5)
        self.assertEquals(Basic.fibonacci(6), 8)
        self.assertEquals(Basic.fibonacci(7), 13)
        self.assertEquals(Basic.fibonacci(8), 21)
        self.assertEquals(Basic.fibonacci(9), 34)
        self.assertEquals(Basic.fibonacci(31), 1346269)

    def test_time_conversion(self):
        self.assertEquals(Basic.time_conversion('07:05:45PM'), '19:05:45')
        self.assertEquals(Basic.time_conversion('12:40:22AM'), '00:40:22')
        self.assertEquals(Basic.time_conversion('12:45:54PM'), '12:45:54')

    def test_multiple_sum(self):
        # 3 5 6 9 10 12 15 18
        self.assertEqual(Basic.multiple_sum(3, 5, 1000), 233168)

    def test_hash_table(self):
        self.assertEqual(Basic.ransom_note('give me one grand today night', 'give one grand today'), True)
        self.assertEqual(Basic.ransom_note('apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg', 'elo lxkvg bg mwz clm w'), True)

    def test_compare_the_triplets(self):
        result = Basic.compare_the_triplets([5, 6, 7], [3, 6, 10])
        self.assertEquals(result, '1 1')


