

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

    def selection_sort_asc(self):
        print('selection_sort(asc) = {}'.upper().format(self.numbers))
        for i in range(len(self.numbers)):
            min_index = i
            for j in range(i, len(self.numbers)):
                if self.numbers[min_index] > self.numbers[j]:
                    min_index = j
            self.numbers[i], self.numbers[min_index] = self.numbers[min_index], self.numbers[i]
            print('min_index[{}] {} = {}'.format(min_index, i, self.numbers))
        return self.numbers

    def selection_sort_desc(self):
        print('selection_sort(desc) = {}'.upper().format(self.numbers))
        for i in range(len(self.numbers)):
            max_index = i
            for j in range(i, len(self.numbers)):
                if self.numbers[max_index] < self.numbers[j]:
                    max_index = j
            self.numbers[i], self.numbers[max_index] = self.numbers[max_index], self.numbers[i]
            print('max_index[{}] {} = {}'.format(max_index, i, self.numbers))
        return self.numbers

    def selection_min(self, k):
        for i in range(len(self.numbers)):
            min_index = i
            for j in range(i, len(self.numbers)):
                if self.numbers[min_index] > self.numbers[j]:
                    min_index = j
            self.numbers[i], self.numbers[min_index] = self.numbers[min_index], self.numbers[i]
            if i == k - 1:
                return self.numbers[i]

    def binary_search_recursive(self, x, left, right):
        if left > right:
            return -1
        mid = int(left + ((right - left) / 2))
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

    def binary_search_iterative(self, x):
        left = 0
        right = len(self.numbers) - 1
        mid = int((left + right) / 2)
        while left <= right:
            if self.numbers[mid] == x:
                return mid
            elif x < self.numbers[mid]:
                right = mid - 1
                mid = int((left + right) / 2)
            elif x > self.numbers[mid]:
                left = mid + 1
                mid = int((left + right) / 2)
            else:
                return -1
        return -1
