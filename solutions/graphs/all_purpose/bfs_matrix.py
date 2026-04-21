from collections import deque

# Length of shortest path from top left to bottom right

class Solution:
    def bfs(self, grid):
        if not grid or not grid[0] or grid[0][0] != 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        queue = deque([[0, 0]])
        grid[0][0] = 0 # Mark as zero

        length = 1 # This lets you count every node in the path, if you want to count edges, start at zero
        while queue:
            n = len(queue)

            for _ in range(n):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length
            
                for dr, dc in directions:
                    if 0 <= (dr + r) < ROWS and 0 <= (dc + c) < COLS and grid[dr + r][dc + c] == 1:
                        queue.append([dr + r, dc + c])
                        grid[dr + r][dc + c] = 0 # If I cannot modify the input, then a visited set is what I should use.
                
            length += 1

        return -1

# Matrix (2D Grid)
grid = [[1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 1, 1]]

print(Solution().bfs(grid))
