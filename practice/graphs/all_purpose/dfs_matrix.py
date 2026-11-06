# Determine if a path exist from the top left to the bottom right.

import pdb

class Solution:
    def find_path(self, grid):
        if not grid or not grid[0] or grid[0][0] != 1:
            return False
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        destination = (ROWS - 1, COLS - 1)

        visited = set()

        def dfs(r, c):
            if (r, c) == destination:
                return True
            
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    if dfs(nr, nc):
                        return True
            
            return False

        return dfs(0, 0)


grid = [[1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 1, 1],
        [1, 1, 1, 1]]

print(Solution().find_path(grid))




































'''
class Solution:
    def find_path(self, grid):
        if not grid or not grid[0] or grid[0][0] != 1:
            return False
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()

        def dfs(r, c):
            if r == ROWS - 1 and c == COLS - 1:
                return True

            visited.add((r, c))
            # NEVER remove from this because it's a "Does a path exist?"
            # problem, not a "Find all paths" problem

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visited and grid[nr][nc] == 1:
                    if dfs(nr, nc):
                        return True
            
            return False

        return dfs(0, 0)
'''
