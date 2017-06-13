"""

"""


class Array(object):
    def __init__(self):
        self.array_list = []

    def __len__(self):
        return len(self.array_list)

    def __str__(self):
        result = '['
        for n in self.array_list:
            result += str(n) + ', '
        return result[:-2] + ']'

    @staticmethod
    def sum(size, numbers):
        if size != len(numbers):
            raise Exception('array size is not matched')
        result = 0
        for number in numbers:
            result += number
        return result

    def sum_string(self, size, array_string):
        numbers = [int(number) for number in array_string.split(' ')]
        if size != len(numbers):
            raise Exception('array size is not matched')
        result = sum(numbers)
        self.array_list = numbers
        return result
