def dfs_preorder_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def dfs_inorder_iterative(root):
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val, end=' ')
        current = current.right

def dfs_postorder_iterative(root):
    if not root:
        return
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        print(stack2.pop().val, end=' ')


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Node(1, Node(2, Node(4), Node(5)), Node(3))
dfs_preorder_iterative(root)
print()
dfs_inorder_iterative(root)
print()
dfs_postorder_iterative(root)
print()
