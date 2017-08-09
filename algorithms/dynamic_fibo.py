

class DynamicFibo:

    def __init__(self):
        self.values = {0: 0, 1: 1}

    def value(self, index):
        if index == 0 or index == 1:
            return self.values[index]
        if index in self.values:
            return self.values[index]
        self.values[index] = self.value(index - 2) + self.value(index - 1)
        return self.values[index]


