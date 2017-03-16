import unittest

from pyalgorithms.data_structures import (
    stack
)

class TestStack(unittest.TestCase):

    def test_stack(self):
        self.stack = stack.Stack()
        self.stack.push(2)
        self.stack.push(4)
        self.stack.push(6)

        self.assertEqual(self.stack.pop(), 6)
        self.assertEqual(self.stack.is_empty(), False)
        self.assertEqual(self.stack.size(), 2)
