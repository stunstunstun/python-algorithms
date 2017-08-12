

class Array(object):
    def __init__(self, array_string):
        self.numbers = [int(number) for number in array_string.split(' ')]

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

    def bubble_sort(self):
        for i in range(len(self.numbers)):
            swapped = False
            for j in range(len(self.numbers) - 1):
                if self.numbers[j] > self.numbers[j + 1]:
                    self.numbers[j], self.numbers[j + 1] = self.numbers[j + 1], self.numbers[j]
                    swapped = True
            if not swapped:
                break
        return self.numbers



