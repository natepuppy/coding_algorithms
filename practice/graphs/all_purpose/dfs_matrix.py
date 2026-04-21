# Determine if a path exist from the top left to the bottom right.

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

grid = [[1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 1, 1],
        [1, 1, 1, 1]]

print(Solution().find_path(grid))


























        # if not grid or not grid[0] or grid[0][0] != 1:
        #     return False

        # ROWS, COLS = len(grid), len(grid[0])
        # directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # # visited = set()
        # # visited.add((0,0))

        # def dfs(r, c):
        #     if r == ROWS - 1 and c == COLS - 1:
        #         return True

        #     # visited.add((r,c))
        #     grid[r][c] = 0

        #     for dr, dc in directions:
        #         new_r = dr + r
        #         new_c = dc + c

        #         if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] != 0: #  and (new_r, new_c) not in visited:
        #             if dfs(new_r, new_c):
        #                 return True
            
        #     return False

        # return dfs(0, 0)