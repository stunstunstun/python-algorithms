"""
    Stack
    -----
    A stack or LIFO (last in, first out) is an abstract data type that serves
    as a collection of elements, with two principal operations: push, which
    adds an element to the collection, and pop, which removes the last element
    that was added.
"""

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


