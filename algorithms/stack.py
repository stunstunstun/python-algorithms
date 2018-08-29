

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
        self.max_size = self.max_size * 2
        new_items = [None] * (self.max_size)
        for index, item in enumerate(self.items):
            new_items[index] = item
        self.items = new_items

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == (self.max_size - 1)

    def has(self, value):
        return value in self.items

BRACKET_PAIRS = {"{": "}", "[": "]", "(": ")"}

def balanced_brackets(expression: str):
    stack = Stack()
    for char in expression:
        if char in BRACKET_PAIRS:
            stack.push(BRACKET_PAIRS[char])
        elif not stack.is_empty() and stack.has(char):
            stack.pop()
        else:
            return False
    return stack.is_empty()

