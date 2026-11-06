class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

def dfs(root):
    print(root.val)

    if root.left:
        dfs(root.left)
    if root.right:
        dfs(root.right)


root = Node(2, Node(1), Node(3))
dfs(root)
