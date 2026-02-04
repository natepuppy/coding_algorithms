def dfs(root):
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val, end=' ')
        current = current.right

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
