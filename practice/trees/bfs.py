from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root: Node) -> None:
    queue = deque([root])

    while queue:
        node = queue.popleft()

        print(node.val)

        if node.left:
            queue.append(node.left)0
        
        if node.right:
            queue.append(node.right)

root = Node(1, Node(2, Node(4), Node(5)), Node(3))
bfs(root)
