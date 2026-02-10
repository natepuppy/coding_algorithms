# Determine if a path exist from the top left to the bottom right.
# You can only move right and down.
def solution(grid):
    if not grid or not grid[0] or grid[0][0] == 1:
        return False
    
    ROWS, COLS = len(grid), len(grid[0])
    memo = {}
    directions = [[1, 0], [0, 1]]

    def dfs(r, c):
        if r == ROWS - 1 and c == COLS - 1:
            return True
        
        if (r, c) in memo:
            return memo[(r, c)]
        
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            
            if (0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 0):
                if dfs(new_r, new_c):
                    memo[(r, c)] = True
                    return True

        memo[(r, c)] = False
        return False

    return dfs(0, 0)

grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

print(solution(grid))
