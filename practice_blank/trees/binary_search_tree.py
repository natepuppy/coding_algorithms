class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    # 1. INSERT (Returns the node after insertion)
    def insert(self, key):
        # Code will be implemented here
        pass

    # 2. SEARCH (Returns True/False)
    def exists(self, key):
        # Code will be implemented here
        pass

    # 3. DELETE (Returns the updated subtree)
    def delete(self, key):
        # Code will be implemented here
        pass

# --- Quick Usage ---
root = Node(50)
for x in [30, 70, 20]: root.insert(x)

print(root.exists(20)) # True
root = root.delete(30) # Always re-assign the root when deleting!
