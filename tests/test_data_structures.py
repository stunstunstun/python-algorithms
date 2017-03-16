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


class TestHashTable(unittest.TestCase):

    def test_string(self):
        name = 'minhyeok'
        hash1 = name.__hash__()
        name = 'minhyeok' + ' jung'
        hash2 = name.__hash__()
        full_name = 'minhyeok jung'
        hash3 = full_name.__hash__()

        self.assertNotEqual(hash1, hash2)
        self.assertEqual(hash2, hash3)
