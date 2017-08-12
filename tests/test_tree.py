import unittest
from algorithms.tree import Node


class TestTree(unittest.TestCase):

    def test_is_binary_search_tree(self):
        tree = Node(4)
        tree.left = Node(2)
        tree.right = Node(6)
        tree.left.left = Node(1)
        tree.left.right = Node(3)
        tree.right.left = Node(5)
        tree.right.right = Node(7)
        self.assertEqual(Node.is_binary_search_tree(tree), True)

        tree = Node(3)
        tree.left = Node(2)
        tree.right = Node(6)
        tree.left.left = Node(1)
        tree.left.right = Node(4)
        tree.right.left = Node(5)
        tree.right.right = Node(7)
        self.assertEqual(Node.is_binary_search_tree(tree), True)
