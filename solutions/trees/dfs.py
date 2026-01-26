def dfs_inorder(root):
    if root:
        dfs_inorder(root.left)
        print(root.val, end=' ')
        dfs_inorder(root.right)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Node(2, Node(1), Node(3))
dfs_inorder(root)
print()

