from collections import deque

# Length of shortest path from top left to bottom right
def bfs(grid):
    length = 0

    ROWS, COLS = len(grid), len(grid[0])

    if ROWS == 0 or COLS == 0 or grid[0][0] == 1:
        return -1

    queue = deque()
    queue.append([0,0])

    neighbors = [[1,0], [-1,0], [0,1], [0,-1]] # optimize directions

    grid[0][0] = 1 # DONT forget the visited

    while queue:
        for i in range(len(queue)):
            current_cell = queue.popleft()

            if current_cell[0] == ROWS - 1 and current_cell[1] == COLS - 1:
                return length
            
            for r, c in neighbors:
                dr = current_cell[0] + r
                dc = current_cell[1] + c

                if not(dr >= ROWS or dr < 0 or dc >= COLS or dc < 0 or grid[dr][dc] == 1):
                    grid[dr][dc] = 1 # DONT forget the visited
                    queue.append([dr, dc])
        
        length += 1
        
    return -1

# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

print(bfs(grid))
