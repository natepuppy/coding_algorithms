from collections import deque

def bfs_level_order(root):
    # Code will be implemented here
    pass


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Node(1, Node(2, Node(4), Node(5)), Node(3))
bfs_level_order(root)
print()
