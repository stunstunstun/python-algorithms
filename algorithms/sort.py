from enum import Enum


class SortType(Enum):
    ASC = 1
    DESC = 2


class Sorting:
    def __init__(self, numbers: list):
        self.numbers = numbers

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

    def merge_sort(self):
        print('merge_sort = {}'.upper().format(self.numbers))
        temp = [0] * len(self.numbers)
        self.merge_sort_recursive(temp, 0, len(self.numbers) - 1)

    def merge_sort_recursive(self, temp, left_start, right_end):
        if left_start >= right_end:
            return
        mid = int((left_start + right_end) / 2)
        self.merge_sort_recursive(temp, left_start, mid)
        self.merge_sort_recursive(temp, mid + 1, right_end)
        self.merge(temp, left_start, right_end)

    def merge(self, temp, left_start, right_end):
        left_end = int((right_end + left_start) / 2)
        right_start = left_end + 1

        size = right_end - left_start + 1
        left = left_start
        right = right_start
        index = left_start
        print('MERGE > left={} right={} index={} size={}'.format(left, right, index, size))
        while left <= left_end and right <= right_end:
            if self.numbers[left] <= self.numbers[right]:
                temp[index] = self.numbers[left]
                left += 1
            else:
                temp[index] = self.numbers[right]
                right += 1
            index += 1

        Sorting.array_copy(self.numbers, left, temp, index, left_end - left + 1)
        Sorting.array_copy(self.numbers, right, temp, index, right_end - right + 1)
        Sorting.array_copy(temp, left_start, self.numbers, left_start, size)
        print(self.numbers)

    @staticmethod
    def array_copy(src: list, src_pos: int, dest: list, dest_pos: int, size: int):
        for i in range(size):
            dest[i + dest_pos] = src[i + src_pos]


