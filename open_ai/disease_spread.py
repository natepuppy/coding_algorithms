
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
        DIRS = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1),
        ]

        doomed = set()          # cells that will die when they resolve
        changed = True

        while changed:
            changed = False

            # Build next round's grid as an independent copy of the current one.
            nxt = copy.deepcopy(self.grid) # This is kinda slow
            
            new_doomed = set()

            for r in range(ROWS):
                for c in range(COLS):
                    cell = self.grid[r][c]

                    if cell == 1:                    # infected -> resolve
                        if (r, c) in doomed:
                            nxt[r][c] = 3            # dies
                        else:
                            nxt[r][c] = 2            # recovers
                    elif cell == 0:                  # susceptible -> maybe infect
                        # Count how many of the eight neighbors are infected.
                        infected_neighbors = 0
                        for dr, dc in DIRS:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < ROWS and 0 <= nc < COLS:
                                if self.grid[nr][nc] == 1:
                                    infected_neighbors += 1

                        if infected_neighbors >= self.infectThreshold:
                            nxt[r][c] = 1
                            changed = True
                            if infected_neighbors >= self.deathThreshold:
                                new_doomed.add((r, c))
                    # cells 2 and 3 are terminal — the row copy already preserves them

            self.grid = nxt
            doomed = new_doomed

        return self.grid