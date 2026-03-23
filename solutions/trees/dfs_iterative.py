class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node):
    # Code will be implemented here
    stack = []
    stack.append(node)

    while stack:
        element = stack.pop() # Remember this returns the last element in the array
        print(element.val)

        if element.right:
            stack.append(element.right)
        if element.left:
            stack.append(element.left)

root = Node(1, Node(2, Node(4), Node(5)), Node(3))
dfs(root)
