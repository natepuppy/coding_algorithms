from pprint import pprint
import pdb

EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2

DIRECTIONS = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1),
    (1,1),
    (-1,1),
    (1,-1),
    (-1,-1)
]

class Othello:
    def __init__(self, size=10):
        # Can't build grid smaller than 4
        self.size = size
        self.grid = self.create_grid()
        self.score = {
            PLAYER_1: 2,
            PLAYER_2: 2
        }

    def print_board(self):
        print(f"Score: Player 1: {self.score[PLAYER_1]} vs. Player 2: {self.score[PLAYER_2]}")
        pprint(self.grid)

    def create_grid(self):
        grid = [[EMPTY] * self.size for _ in range(self.size)]
        mid = self.size // 2 - 1

        grid[mid][mid] = PLAYER_1
        grid[mid + 1][mid + 1] = PLAYER_1
        grid[mid + 1][mid] = PLAYER_2
        grid[mid][mid + 1] = PLAYER_2

        return grid

    def game_over(self):
        if self.valid_moves(PLAYER_1) == self.valid_moves(PLAYER_2) == []:
            return True
        return False
    
    def oob(self, r, c):
        return not (0 <= r < self.size and 0 <= c < self.size)

    def capture(self, player, r, c):
        if self.oob(r, c) or self.grid[r][c] != EMPTY:
            return []
        
        cells_captured = []

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            cells = []

            while not self.oob(nr, nc):
                value = self.grid[nr][nc]
                
                if value == player:
                    cells_captured += cells
                    break
                
                if value == EMPTY:
                    break
                
                cells.append((nr, nc))

                nr += dr
                nc += dc
        
        return cells_captured

    def execute_move(self, player, opponent, r, c):
        cells_captured = self.capture(player, r, c)

        if not cells_captured:
            return False

        for nr, nc in cells_captured:
            self.score[player] += 1
            self.score[opponent] -= 1
            self.grid[nr][nc] = player
        
        self.grid[r][c] = player
        self.score[player] += 1
        
        return True

    def valid_moves(self, player):
        moves = []

        for r in range(self.size):
            for c in range(self.size):
                if len(self.capture(player, r, c)) > 0:
                    moves.append((r,c))
        
        return moves

    def get_user_input(self, player):
        while True:
            try:
                r = int(input(f"Row Number: Please in put number from 0-{self.size - 1}: "))
                c = int(input(f"Column Number: Please in put number from 0-{self.size - 1}: "))

                if (r, c) in self.valid_moves(player):
                    return (r, c)
                else:
                    print("Invalid move. Please Try Again")
                    continue
                
            except ValueError:
                print("Invalid move. Please Try Again")
                continue

    def play(self):
        player = PLAYER_1
        opponent = PLAYER_2

        while not self.game_over():
            if self.valid_moves(player):
                self.print_board()
                r, c = self.get_user_input(player)
                self.execute_move(player, opponent, r, c)
            else:
                print(f"Player {player} does not have a valid more.")

            player, opponent = opponent, player

        print("Game Finished:")

        winner = None
        if self.score[PLAYER_1] > self.score[PLAYER_2]:
            winner = PLAYER_1
        elif self.score[PLAYER_2] > self.score[PLAYER_1]:
            winner = PLAYER_2
        else:
            print("It is a tie!")
        
        if winner:
            print(f"Winning is player: {winner}")


        self.print_board()

if __name__ == "__main__":
    Othello().play()
