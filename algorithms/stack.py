import copy

class Stack:
    def __init__(self, max_size=10):
        self.items = [None] * max_size
        self.max_size = max_size
        self.top = -1

    def push(self, item):
        if self.is_full():
            self.expand()
        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item

    def expand(self):
        new_items = [None] * (self.max_size * 2)
        for index, item in enumerate(self.items):
            new_items[index] = item
        self.items = new_items

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == (self.max_size - 1)

    def has(self, value):
        return value in self.items

    @staticmethod
    def balanced_brackets(expression: str):
        pairs = {"{": "}", "[": "]", "(": ")"}

        stack = Stack()
        for char in expression:
            if char in pairs:
                stack.push(pairs[char])
            elif not stack.is_empty() and stack.has(char):
                stack.pop()
            else:
                return False
        return stack.is_empty()


