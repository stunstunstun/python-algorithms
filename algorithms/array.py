

class Array(object):
    def __init__(self, numbers):
        self.numbers = numbers

    def __len__(self):
        return len(self.numbers)

    def __str__(self):
        result = '['
        for n in self.numbers:
            result += str(n) + ', '
        return result[:-2] + ']'

    def sum(self, size):
        if size != len(self.numbers):
            raise Exception('array size is not matched')
        result = sum(self.numbers)
        return result

    def rotate(self, shift):
        head = shift % len(self.numbers)
        self.numbers = self.numbers[head:] + self.numbers[:head]
        return self.numbers

    @staticmethod
    def pop(numbers):
        numbers.pop()


