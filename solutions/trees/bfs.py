

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def bfs(root):
    queue = deque()

    queue.append(root)

    while queue:
        node = queue.popleft()

        print(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = Node(1, Node(2, Node(4), Node(5)), Node(3))
bfs(root)
print()
