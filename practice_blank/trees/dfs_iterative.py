def dfs_preorder_iterative(root):
    # Code will be implemented here
    pass

def dfs_inorder_iterative(root):
    # Code will be implemented here
    pass

def dfs_postorder_iterative(root):
    # Code will be implemented here
    pass


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Node(1, Node(2, Node(4), Node(5)), Node(3))
dfs_preorder_iterative(root)
print()
dfs_inorder_iterative(root)
print()
dfs_postorder_iterative(root)
print()
