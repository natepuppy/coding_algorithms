# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a 
# complete binary tree, and all nodes in the last level are as far left as possible. It can 
# have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self._left_height(root)
        right_height = self._right_height(root)

        # If both spines are equal, it's a perfect tree: 2^h - 1 nodes
        if left_height == right_height:
            return (1 << left_height) - 1

        # Otherwise recurse — one subtree is guaranteed perfect
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def _left_height(self, node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h

    def _right_height(self, node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h







