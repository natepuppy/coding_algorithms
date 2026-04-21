class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root):
    if not root: # Dont forget this
        return None
    
    print(root.val)
    dfs(root.left)
    dfs(root.right)

root = Node(2, Node(1), Node(3))
dfs(root)
