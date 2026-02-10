import collections

def pretty_print(root):
    if not root:
        print("Empty Tree")
        return

    # 1. Map out the tree into levels
    levels = []
    queue = collections.deque([(root, 0)])
    while queue:
        node, depth = queue.popleft()
        if len(levels) <= depth:
            levels.append([])
        levels[depth].append(node)
        
        if node:
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
        else:
            # Add placeholders for children of None nodes to keep the grid
            queue.append((None, depth + 1))
        
        # Stop if the next level is entirely None
        if all(n is None for n, d in queue):
            break

    # 2. Calculate spacing
    depth = len(levels)
    max_width = 2**depth * 4
    
    print("\n--- Tree Visualization ---")
    for i, level in enumerate(levels):
        # Spacing between nodes at this level
        gap = max_width // (2**i)
        line = ""
        for node in level:
            val = str(node.val) if node else " "
            line += val.center(gap)
        print(line)
        
        # Add "branches" (optional)
        if i < depth - 1:
            branches = ""
            for node in level:
                b = "/  \\" if node else "    "
                branches += b.center(gap)
            print(branches)
    print("--------------------------\n")

class Node:
    def __init__(self, val, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right
    
    def insert(self, val):
        if val <= self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)

    def search(self, val):
        if val < self.val:
            if self.left:
                return self.left.search(val)
        elif val > self.val:
            if self.right:
                return self.right.search(val)
        elif val == self.val:
            return True

        return False
            

    def delete():
        pass


# --- Quick Usage ---
root = Node(30)
root.insert(45)
root.insert(35)
root.insert(25)
root.insert(20)
root.insert(15)

pretty_print(root)

print(root.search(15))
print(root.search(35))
print(root.search(30))
print(root.search(25))



# print(root.exists(20)) # True
# root = root.delete(30) # Always re-assign the root when deleting!
