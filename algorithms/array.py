from enum import Enum


class SortType(Enum):
    ASC = 1
    DESC = 2


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
        print('bubble_sort = {}'.upper().format(self.numbers))
        for i in range(len(self.numbers)):
            swapped = False
            for j in range(len(self.numbers) - 1):
                if self.numbers[j] > self.numbers[j + 1]:
                    self.numbers[j], self.numbers[j + 1] = self.numbers[j + 1], self.numbers[j]
                    swapped = True
            if not swapped:
                break
            print('{}'.format(self.numbers))
        return self.numbers

    def selection_sort(self, sort_type=SortType.ASC):
        print('selection_sort(type={}) = {}'.upper().format(sort_type, self.numbers))
        for i in range(len(self.numbers)):
            index = i
            for j in range(i, len(self.numbers)):
                if sort_type == SortType.ASC and self.numbers[index] > self.numbers[j]:
                    index = j
                if sort_type == SortType.DESC and self.numbers[index] < self.numbers[j]:
                    index = j
            self.numbers[i], self.numbers[index] = self.numbers[index], self.numbers[i]
            print('index[{}] {} = {}'.format(index, i, self.numbers))
        return self.numbers

    def selection(self, k, sort_type=SortType.ASC):
        for i in range(len(self.numbers)):
            index = i
            for j in range(i, len(self.numbers)):
                if sort_type == SortType.ASC and self.numbers[index] > self.numbers[j]:
                    index = j
                if sort_type == SortType.DESC and self.numbers[index] < self.numbers[j]:
                    index = j
            self.numbers[i], self.numbers[index] = self.numbers[index], self.numbers[i]
            if i == k - 1:
                return self.numbers[i]

    def binary_search_recursive(self, x, left, right):
        if left > right:
            return -1
        mid = int(left + (right - left) / 2)
        if self.numbers[mid] == x:
            return mid
        elif x < self.numbers[mid]:
            return self.binary_search_recursive(x, left, mid - 1)
        elif x > self.numbers[mid]:
            return self.binary_search_recursive(x, mid + 1, right)
        else:
            return -1

    def binary_search(self, x):
        return self.binary_search_recursive(x, 0, len(self.numbers) - 1)
