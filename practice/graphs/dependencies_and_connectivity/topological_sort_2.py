
'''
process all leaf nodes of this tree. Then process all the new leaf nodes, 
then process the new leaf nodes etc... You cannot modify the tree at all

      1
    /  \
   2    3
       / \
      4   5

possible results:
[2, 4, 5, 3, 1]
[5, 4, 2, 3, 1]

not valid:
[4,5,3,2,1]

'''


from collections import defaultdict

class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children or []

def process_leaves(root):
    buckets = defaultdict(list)  # height -> list of node values

    def height(node):
        # A leaf has height 0; any other node is 1 above its tallest child.
        node_height = 0
        if node.children:
            child_heights = []

            for child in node.children:
                child_heights.append(height(child))
            
            tallest_child = max(child_heights)
            node_height = tallest_child + 1

        buckets[node_height].append(node.val)
        return node_height

    if root:
        height(root)

    result = []
    for h in sorted(buckets):          # ascending: leaves first
        result.extend(buckets[h])      # order within a level is arbitrary
    return result



from collections import deque

# Khans Algorithm
def process_leaves_2(root):
    if not root:
        return []

    degree = {}
    parent = {}

    def dfs(node):
        degree[node] = len(node.children)
        for child in node.children:
            parent[child] = node
            dfs(child)

    dfs(root)

    # Initial leaves: every node with no children (degree[node] == 0).
    queue = deque()
    for node in degree:
        if degree[node] == 0:
            queue.append(node)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node in parent:
            p = parent[node]
            degree[p] -= 1

            if degree[p] == 0:
                queue.append(p)

    return result




