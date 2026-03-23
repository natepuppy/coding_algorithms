class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(node, val):
    if not node:
        return Node(val)
    
    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node

def search(node, val):
    if not node:
        return False
        
    if val == node.val:
        return True

    if val < node.val:
        return search(node.left, val)
    else:
        return search(node.right, val)

def delete(root, val):
    if not root:
        return None
    
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        temp = find_min(root.right)

        root.val = temp.val

        root.right = delete(root.right, temp.val)
    return root

def find_min(node):
    while node.left:
        node = node.left
    return node


# --- Test ---
root = None
for x in [50, 30, 70, 20, 40]:
    root = insert(root, x)

print(search(root, 20))   # True
print(search(root, 99))   # False
root = delete(root, 30)
print(search(root, 30))   # False
