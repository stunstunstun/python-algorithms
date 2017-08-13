

class DP:

    def __init__(self, max_size=100):
        self.values = [0] * max_size
        self.values[1] = 1

    def fibonacci(self, index):
        if index == 0 or index == 1:
            return self.values[index]
        if self.values[index] != 0:
            return self.values[index]
        self.values[index] = self.fibonacci(index - 2) + self.fibonacci(index - 1)
        return self.values[index]


