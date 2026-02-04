class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 

def dfs(node):
    # Do this just to be safe...
    if not node:
        return

    dfs(node.left)
    print(node.val)
    dfs(node.right)

root = Node(2, Node(1), Node(3))
dfs(root)
