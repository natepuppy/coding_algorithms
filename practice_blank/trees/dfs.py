def dfs_inorder(root):
    # Code will be implemented here
    pass


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Node(2, Node(1), Node(3))
dfs_inorder(root)
print()
