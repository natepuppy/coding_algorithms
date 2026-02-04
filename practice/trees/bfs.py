from collections import deque

class Node:
    def __init__(self, val, left=None, right=None): # Dont forget to put the default Nones here
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
    # DONT Forget this!!!!! # Or else, you will put [None] into the queue
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft() # popleft

        print(node.val)

        if node.left: # Remeber to use node, NOT root here.
            queue.append(node.left) # append

        if node.right:
            queue.append(node.right)

root = Node(1, Node(2, Node(4), Node(5)), Node(3))
bfs(root)
print()
