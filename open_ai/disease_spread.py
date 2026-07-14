
import copy

class Solution:
    def __init__(self, grid, infectThreshold, deathThreshold):
        self.grid = grid
        self.infectThreshold = infectThreshold
        self.deathThreshold = deathThreshold

    def run(self):
        if not self.grid or not self.grid[0]:
            return self.grid

        ROWS, COLS = len(self.grid), len(self.grid[0])
        directions = [
            [-1, -1], 
            [-1, 0], 
            [-1, 1], 
            [1, -1], 
            [1, 0], 
            [1, 1], 
            [0, -1], 
            [0, 1]
        ]

        death_mark = [[False] * COLS for _ in range(ROWS)]
        any_cells_updated = True

        while any_cells_updated:
            any_cells_updated = False
            tomorrow = copy.deepcopy(self.grid)
            new_death_mark = [[False] * COLS for _ in range(ROWS)]

            for r in range(ROWS):
                for c in range(COLS):
                    if self.grid[r][c] in (2, 3):
                        continue
                    elif self.grid[r][c] == 1: # resolve infected cells
                        if death_mark[r][c]:
                            tomorrow[r][c] = 3
                        else:
                            tomorrow[r][c] = 2
                        continue

                    infected_neighbors = 0

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            if self.grid[nr][nc] == 1:
                                infected_neighbors += 1

                    if infected_neighbors >= self.infectThreshold:
                        tomorrow[r][c] = 1
                        any_cells_updated = True

                        if infected_neighbors >= self.deathThreshold:
                            new_death_mark[r][c] = True

            self.grid = tomorrow
            death_mark = new_death_mark

        return self.grid