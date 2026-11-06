class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root):
    if root is None:
        return
    
    dfs(root.left)
    print(root.val)
    dfs(root.right)
    

root = Node(2, Node(1), Node(3))
dfs(root)
