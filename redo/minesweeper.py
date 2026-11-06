# 20 min so far

from pprint import pprint
import random
from collections import deque
import pdb

OPEN = 0
BOMB = -1
COVERED = 1
UNCOVERED = 0

DIRECTIONS = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 1],
    [-1, -1],
    [-1, 1],
    [1, -1],
]

class Minesweeper():
    def __init__(self, rows=10, cols=10, bombs=3):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.grid = self.build_grid()
        self.grid_masked = [[COVERED] * self.cols for _ in range(self.rows)]

        # self.print_board()

    def print_board(self):
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                if self.grid_masked[r][c] == UNCOVERED:
                    row.append(str(self.grid[r][c]))
                else:
                    row.append("X")
            print(" ".join(row)) # I dont know why this works

    def oob(self, r, c):
        return not (0 <= r < self.rows and 0 <= c < self.cols)

    def place_bombs(self, grid):
        bomb_locations = set()

        while len(bomb_locations) < self.bombs:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)

            bomb_locations.add((r,c))
        
        for r, c in bomb_locations:
            grid[r][c] = BOMB

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if self.oob(nr, nc) or grid[nr][nc] == -1:
                    continue
                grid[nr][nc] += 1

        return grid

    def build_grid(self):
        grid = [[OPEN] * self.cols for _ in range(self.rows)]

        grid = self.place_bombs(grid)

        return grid
    
    def get_input(self):
        while True:
            try:
                r = int(input("Please input the row number: "))
                c = int(input("Please input the column number: "))

                if self.oob(r, c):
                    print("Invalid input. Please input something within range.")
                    continue
                
                if self.grid_masked[r][c] == UNCOVERED:
                    print("Invalid input. Please inchoose a cell that has not been uncovered.")
                    continue

                return (r, c)

            except ValueError:
                print("Invalid input. Input nust be integers")
                continue

    def game_over(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid_masked[r][c] == COVERED and self.grid[r][c] != -1:
                    return False
        
        return True

    def uncover(self, r, c):
        self.grid_masked[r][c] = UNCOVERED

        queue = deque()
        queue.append((r, c))

        while queue:
            r, c = queue.popleft()

            # pdb.set_trace()

            if self.grid[r][c] != 0:
                continue

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc

                if (not self.oob(nr, nc)) and self.grid_masked[nr][nc] == COVERED and self.grid[nr][nc] != BOMB:
                    queue.append((nr, nc))
                    self.grid_masked[nr][nc] = UNCOVERED


    def execute_move(self, r, c):
        if self.grid[r][c] == BOMB:
            self.grid_masked[r][c] = UNCOVERED
            return True
        
        self.uncover(r, c)

        return False



    def play(self):
        win = True
        self.print_board()

        while not self.game_over():
            r, c = self.get_input()
            if self.execute_move(r, c):
                win = False
                break
            
            self.print_board()

        if win:
            print("You won!")
        else:
            print("You lost!")
        self.print_board()
        




if __name__ == "__main__":
    minesweeper = Minesweeper()
    minesweeper.play()





