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
        array = Array(3, [3, 2, 1])
        array.bubble_sort()

        number_of_swaps = array.number_of_swaps
        numbers = array.numbers

        self.assertEqual(array.number_of_swaps, 3)
        self.assertEqual(array.numbers, [1, 2, 3])

        print('Array is sorted in {} swaps.'.format(number_of_swaps))
        print('First Element: {}'.format(numbers[0]))
        print('Last Element: {}'.format(numbers[array.size - 1]))


if __name__ == "__main__":
    unittest.main()
