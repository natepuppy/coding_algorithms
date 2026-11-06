class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root: Node) -> None:
    stack = []
    node = root

    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        print(node.val)

        node = node.right

root = Node(1, Node(2, Node(4), Node(5)), Node(3))
dfs(root)
