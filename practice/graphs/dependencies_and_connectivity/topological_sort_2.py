
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

def top_sort(root):
    result = []
    master_visited = set()

    def dfs(node, visited):
        if (node.left is None and node.right is None) or (node.left in master_visited and node.right in master_visited):
            result.append(node)
            visited.add(node)
            return visited
        
        if node.left is not None:
            dfs(node.left, visited)
        
        if node.right is not None:
            dfs(node.right, visited)
        
        return visited
    
    while root not in master_visited:
        res = dfs(root)
        master_visited.add(res)










from collections import deque

def process_leaves(root):
    degree = {}
    parent = {}

    # Build maps
    def dfs(node):
        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        degree[node] = (1 if node.left else 0) + (1 if node.right else 0)

        if node.left:
            parent[node.left] = node
        if node.right:
            parent[node.right] = node

        return degree[node]

    dfs(root)

    # Start with leaves
    queue = deque([node for node in degree if degree[node] == 0])
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




