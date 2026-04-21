class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root: Node) -> None:
    if not root:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val)

        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)


root = Node(1, Node(2, Node(4), Node(5)), Node(3))
dfs(root)
