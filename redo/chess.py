from pprint import pprint

WHITE, BLACK = "w", "b"
SIZE = 8
PIECE_ORDER = ["r", "n", "b", "q", "k", "b", "n", "r"]
FORWARD = {WHITE: -1, BLACK: 1}
PAWN_START = {
    WHITE: 6, BLACK: 1
}
DIRECTIONS = {
    "n": [(2,1), (2,-1), (1,2), (1,-2), (-2,1), (-2,-1), (-1,2), (-1,-2)],
    "r": [(1,0), (0,1), (-1,0), (0,-1)],
    "b": [(1,1), (-1,-1), (-1,1), (1,-1)],
    "q": [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)],
    "k": [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]
}

class Chess:
    def __init__(self):
        self.grid = self.build_grid()
        self.print_grid()
        self.player = WHITE
        self.opponent = BLACK

    def build_grid(self):
        grid = [[("", "")] * SIZE for _ in range(SIZE)]

        for col in range(len(PIECE_ORDER)):
            piece = PIECE_ORDER[col]
            grid[0][col] = (BLACK, piece)
            grid[1][col] = (BLACK, "p")
            grid[6][col] = (WHITE, "p")
            grid[7][col] = (WHITE, piece)

        return grid
    
    def in_bounds(self, r, c):
        return 0 <= r < SIZE and 0 <= c < SIZE

    # Come back to this
    def print_grid(self):
        print("    " + "  ".join(map(str, range(SIZE))))

        for row in range(SIZE):
            cells = [".." if not piece[0] else piece[0][0] + piece[1] for piece in self.grid[row]]
            print(row, " ", " ".join(cells))

    def execute_move(self, r, c, dest_r, dest_c):
        piece = self.grid[r][c][1]
        self.grid[r][c] = ("", "")
        self.grid[dest_r][dest_c] = (self.player, piece)

    def king_in_check(self, player):
        # Find the King
        king = None
        for r in range(SIZE):
            for c in range(SIZE):
                player_num, piece = self.grid[r][c]
                if player_num == player and piece == "k":
                    king = (r, c)
                    break
            if king:
                break

        if king is None:
            return True
        
        # Determine the opponent
        if player == WHITE:
            opponent = BLACK
        else:
            opponent = WHITE

        # Determine if you this move puts yourself in check
        # Calling valid_moves(opponent) would cause infinite loop
        for r in range(SIZE):
            for c in range(SIZE):
                if self.grid[r][c][0] != opponent:
                    continue
                for _, _, tr, tc in self.valid_moves_for_piece(r, c, check=False):
                    if (tr, tc) == king:
                        return True
        
        return False

    def puts_player_in_check(self, fr, fc, tr, tc):
        player_f, piece_f = self.grid[fr][fc]
        player_t, piece_t = self.grid[tr][tc]

        self.grid[fr][fc] = ("", "")
        self.grid[tr][tc] = (player_f, piece_f)

        in_check = self.king_in_check(player_f) # Use player_f

        self.grid[fr][fc] = (player_f, piece_f)
        self.grid[tr][tc] = (player_t, piece_t)

        return in_check

    def valid_moves_for_piece(self, r, c, check=True):
        player, piece = self.grid[r][c]
        destinations = []

        if piece == "p":
            forward = FORWARD[player]

            # Attacks
            for dc in (-1, 1):
                nr, nc = r + forward, c + dc

                # OOB or no opponent to kill
                if not self.in_bounds(nr, nc) or self.grid[nr][nc][0] in ["", player]:
                    continue
                
                destinations.append((nr, nc))
            
            # Move one space
            nr, nc = r + forward, c
            can_move_one_space = self.in_bounds(nr, nc) and self.grid[nr][nc][0] == ""
            if can_move_one_space:
                destinations.append((nr, nc))
            
            # Can move two spaces?
            nr = r + (forward * 2)
            if r == PAWN_START[player] and can_move_one_space and self.in_bounds(nr, c) and self.grid[nr][c][0] == "":
                destinations.append((nr, c))
        else:
            move_limit = SIZE - 1
            if piece in ["k", "n"]:
                move_limit = 1
            
            for dr, dc in DIRECTIONS[piece]:
                nr, nc = r + dr, c + dc

                for _ in range(move_limit):
                    if not self.in_bounds(nr, nc):
                        break
                    occupant = self.grid[nr][nc][0]
                    if occupant == player:
                        break
                    destinations.append((nr, nc))
                    if occupant != "":
                        break

                    nr, nc = nr + dr, nc + dc
        
        moves = []
        for tr, tc in destinations:
            if check and self.puts_player_in_check(r, c, tr, tc): # Dont forget the "check" param here!!!!!
                continue
            moves.append((r, c, tr, tc))
        return moves

    def valid_moves(self, player):
        moves = set()
        for r in range(SIZE):
            for c in range(SIZE):
                if self.grid[r][c][0] == player: # Check it is the player's piece
                    moves.update(self.valid_moves_for_piece(r, c))
        
        return moves

    def play(self):
        while True:
            moves = self.valid_moves(self.player)

            if not moves:
                break
            
            print(f"Valid moves: {sorted(moves)}")

            try:
                fr = int(input("Input piece's current row: "))
                fc = int(input("Input piece's current column: "))
                tr = int(input("Input piece's destination row: "))
                tc = int(input("Input piece's destination column: "))

                if (fr, fc, tr, tc) not in moves:
                    print("Invalid Move")
                    continue

                self.execute_move(fr, fc, tr, tc)
                self.player, self.opponent = self.opponent, self.player

                self.print_grid()

            except ValueError:
                print("Please input valid integers")
        
        self.print_grid()

        if self.king_in_check(self.player):
            print(f"{self.opponent} wins")
        else:
            print("Tie")

if __name__ == "__main__":
    game = Chess()
    game.play()
