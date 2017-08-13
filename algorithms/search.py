

class Search:

    @staticmethod
    def binary_search_iterative(numbers, x):
        left = 0
        right = len(numbers) - 1
        mid = int(left + (right - left) / 2)
        while left <= right:
            if numbers[mid] == x:
                return mid
            elif x < numbers[mid]:
                right = mid - 1
                mid = int(left + (right - left) / 2)
            elif x > numbers[mid]:
                left = mid + 1
                mid = int(left + (right - left) / 2)
            else:
                return -1
        return -1

    @staticmethod
    def index(flavors: list, value, exclude):
        for i in range(0, len(flavors)):
            if flavors[i] == value and i != exclude:
                return i
        return -1

    @staticmethod
    def ice_cream_parlor(money, flavors: list):
        """
        https://www.hackerrank.com/challenges/ctci-ice-cream-parlor        
        """
        sorted_flavors = sorted(flavors)
        for i, flavor in enumerate(sorted_flavors):
            complement = money - flavor
            location = Search.binary_search_iterative(sorted_flavors, complement)
            if 0 <= location < len(sorted_flavors):
                a = Search.index(flavors, sorted_flavors[i], -1)
                b = Search.index(flavors, complement, a)
                return ' '.join(map(lambda x: str(x), [min(a + 1, b + 1), max(a + 1, b + 1)]))