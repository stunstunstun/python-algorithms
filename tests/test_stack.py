import unittest
from algorithms.stack import Stack, balanced_brackets


class TestStack(unittest.TestCase):

    def test_stack(self):
        stack = Stack()
        stack.push(2)
        stack.push(4)
        stack.push(6)

        self.assertEqual(stack.pop(), 6)
        self.assertEqual(stack.is_empty(), False)   
        self.assertEqual(stack.top, 1)
        self.assertEqual(stack.has(4), True)
        self.assertEqual(stack.is_full(), False)

        for i in range(8):
            stack.push(i)
        self.assertEqual(stack.is_full(), True)
        self.assertEqual(stack.top, stack.max_size - 1)

        for i in range(10):
            stack.push(i)
        self.assertEqual(stack.is_full(), True)
        self.assertEqual(stack.top, stack.max_size - 1)

    def test_balanced_brackets(self):
        self.assertEqual(balanced_brackets('{[()]}'), True)
        self.assertEqual(balanced_brackets('}][}}(}][))]'), False)
        self.assertEqual(balanced_brackets('[](){()}'), True)
        self.assertEqual(balanced_brackets('({}([][]))[]()'), True)
        self.assertEqual(balanced_brackets('{)[](}]}]}))}(())('), False)
