class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    # 1. INSERT (Returns the node after insertion)
    def insert(self, key):
        if key < self.val:
            self.left = self.left.insert(key) if self.left else Node(key)
        elif key > self.val:
            self.right = self.right.insert(key) if self.right else Node(key)
        return self

    # 2. SEARCH (Returns True/False)
    def exists(self, key):
        if key == self.val: return True
        if key < self.val and self.left: return self.left.exists(key)
        if key > self.val and self.right: return self.right.exists(key)
        return False

    # 3. DELETE (Returns the updated subtree)
    def delete(self, key):
        if key < self.val:
            if self.left: self.left = self.left.delete(key)
        elif key > self.val:
            if self.right: self.right = self.right.delete(key)
        else:
            # Node found! 
            if not self.left: return self.right  # Case: 0 or 1 child
            if not self.right: return self.left
            
            # Case: 2 children (Find successor)
            temp = self.right
            while temp.left: temp = temp.left
            self.val = temp.val
            self.right = self.right.delete(temp.val)
        return self

# --- Quick Usage ---
root = Node(50)
for x in [30, 70, 20]: root.insert(x)

print(root.exists(20)) # True
root = root.delete(30) # Always re-assign the root when deleting!