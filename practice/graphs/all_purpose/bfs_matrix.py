from collections import deque
# Length of shortest path from top left to bottom right

# Use a global visited set if you should only visit a node once
# --- Then never remove from it
# Use a global visiting set if you only want to visit a node once in a path
# --- Remove it from the set at the bottom of the loop, so it can be used in different paths

class Solution:
    def bfs(self, grid):
        if not grid or not grid[0] or grid[0][0] != 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = deque()
        count = 0 # set count=1 if I want to count the number of nodes

        queue.append((0,0))
        visited = set()
        visited.add((0,0)) # Dont forget to add this!!!!!

        while queue:
            for _ in range(len(queue)): # YOU NEED THIS for counting by level!!!!!
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return count

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                
            count += 1

        return -1

# Matrix (2D Grid)
grid = [[1, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 1, 1]]

print(Solution().bfs(grid))
