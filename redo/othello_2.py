from pprint import pprint
import pdb

EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2
GRID_SIZE = 8
DIRECTIONS = [
    [1,0],
    [0,1],
    [-1,0],
    [0,-1],
    [1,1],
    [-1,-1],
    [1,-1],
    [-1,1]
]

class Othello:
    def __init__(self, size):
        self.size = size
        self.grid = self.build_grid()
        self.score = {
            PLAYER_1: 2,
            PLAYER_2: 2
        }
    
    def build_grid(self):
        grid = [[EMPTY] * self.size for _ in range(self.size)]

        mid = self.size // 2

        grid[mid - 1][mid - 1] = PLAYER_1
        grid[mid][mid] = PLAYER_1
        grid[mid - 1][mid] = PLAYER_2
        grid[mid][mid - 1] = PLAYER_2

        return grid
    
    def print_grid(self):
        pprint(self.grid)
    
    def in_bounds(self, r, c):
        return (0 <= r < self.size and 0 <= c < self.size)

    def capture(self, player, opponent, r, c):
        if self.grid[r][c] != EMPTY:
            return []
        
        captured_cells = []
        
        for dr, dc in DIRECTIONS:
            cells_to_capture = []
            nr, nc = dr + r, dc + c

            while self.in_bounds(nr, nc) and self.grid[nr][nc] == opponent:
                cells_to_capture.append((nr, nc))
                nr, nc = dr + nr, dc + nc
            
            if self.in_bounds(nr, nc) and self.grid[nr][nc] == player:
                captured_cells += cells_to_capture

        if captured_cells:
            captured_cells.append((r, c))

        return captured_cells
    
    def game_over(self):
        if self.valid_moves(PLAYER_1, PLAYER_2) == self.valid_moves(PLAYER_2, PLAYER_1) == []:
            return True
        return False
    
    def valid_moves(self, player, opponent):
        result = []
        for r in range(self.size):
            for c in range(self.size):
                if self.capture(player, opponent, r, c):
                    result.append((r, c))
        return result

    def execute_move(self, player, opponent, r, c):
        cells = self.capture(player, opponent, r, c)
        self.score[player] += len(cells)
        self.score[opponent] -= (len(cells) - 1)
        self.convert(player, cells)

    def convert(self, player, cells):
        for r, c in cells:
            self.grid[r][c] = player

    def play(self):
        player = PLAYER_1
        opponent = PLAYER_2

        self.print_grid()

        while not self.game_over():
            moves = self.valid_moves(player, opponent)

            if not moves:
                player, opponent = opponent, player
                continue
                
            print(f"Player {player}'s Turn:")
            print(f"Valid moves: {moves}")

            # Assume the input is valid
            r = int(input("Input your move's row: "))
            c = int(input("Input your move's column: "))

            self.execute_move(player, opponent, r, c)

            self.print_grid()

            player, opponent = opponent, player
        
        if self.score[PLAYER_1] > self.score[PLAYER_2]:
            print("PLAYER 1 WINS")
        elif self.score[PLAYER_2] > self.score[PLAYER_1]:
            print("PLAYER 2 WINS")
        else:
            print("Tie")
        


if __name__ == "__main__":
    game = Othello(GRID_SIZE)
    game.play()
