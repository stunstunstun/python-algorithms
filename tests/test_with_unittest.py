"""
available by this command
$ python3 tests/test_with_unittest.py
"""
import unittest


class Array:
    
    def __init__(self, size, numbers):
        self.number_of_swaps = 0
        self.size = size
        self.numbers = numbers
        self.count = 0

    def bubble_sort(self):
        for i in range(self.size):
            is_swap = False
            for j in range(self.size - 1):
                self.count += 1
                if self.numbers[j] > self.numbers[j + 1]:
                    self.numbers[j], self.numbers[j + 1] = self.numbers[j + 1], self.numbers[j]
                    self.number_of_swaps += 1
                    is_swap = True
            if not is_swap:
                break


class TestArray(unittest.TestCase):

    def test_bubble_sort(self):
        numbers = [3, 10, 9, 2, 100, 1, 99, 1000, 232, 7]
        print(numbers)
        array = Array(10, numbers)
        array.bubble_sort()

        number_of_swaps = array.number_of_swaps
        numbers = array.numbers

        self.assertEqual(array.number_of_swaps, 17)
        self.assertEqual(array.numbers, [1, 2, 3, 7, 9, 10, 99, 100, 232, 1000])

        print('Array is sorted in {} swaps.'.format(number_of_swaps))
        print(array.numbers)

if __name__ == "__main__":
    unittest.main()
