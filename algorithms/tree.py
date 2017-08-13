"""
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
"""


class Node:

    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

    @classmethod
    def check_bst(cls, root, min_value, max_value):
        if root is None:
            return True
        return (
            min_value < root.value < max_value and
            Node.check_bst(root.left, min_value, root.value) and
            Node.check_bst(root.right, root.value, max_value))

    @classmethod
    def is_binary_search_tree(cls, root):
        return Node.check_bst(root, -float('inf'), float('inf'))


