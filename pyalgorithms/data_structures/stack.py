class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        return self.stack_list.pop()

    def is_empty(self):
        return not self.size()

    def size(self):
        return len(self.stack_list)
