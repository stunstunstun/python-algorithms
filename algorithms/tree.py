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
    def check_bst(cls, root):
        if root.left and root.left.value >= root.value:
            return False
        if root.right and root.right.value <= root.value:
            return False
        return True

    @classmethod
    def is_binary_search_tree(cls, root):
        if not cls.check_bst(root):
            return False
        if root.left:
            cls.is_binary_search_tree(root.left)
        if root.right:
            cls.is_binary_search_tree(root.right)


        return True


