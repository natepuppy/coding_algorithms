import pdb
from pprint import pprint
from unittest.mock import patch

WATER = "W"
SHIP = "S"
HIT = "H"
MISS = "M"
SHIP_LENGTHS = [2, 3]

PLAYER_1 = 1
PLAYER_2 = 2



class Battleship:
    def __init__(self, ships, rows=10, cols=10):
        self.ships = ships
        self.rows = rows
        self.cols = cols

        self.board_1 = self.build_board()
        self.board_2 = self.build_board()



    def build_board(self):
        return [[WATER] * self.cols for _ in range(self.rows)]

    ########################################## PRINTING ##########################################
    def print_boards(self):
        self.print_player_1_full_board()
        self.print_player_2_full_board()

    def print_player_1_full_board(self):
        print("Player 1 Board")
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(self.board_1[r][c])
            print(" ".join(row))

    def print_player_2_full_board(self):
        print("Player 2 Board")
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(self.board_2[r][c])
            print(" ".join(row))

    def print_misses_player_1(self):
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                if self.board_1[r][c] == HIT:
                    row.append(HIT)
                elif self.board_1[r][c] == MISS:
                    row.append(MISS)
                else:
                    row.append(WATER)
            print(" ".join(row))

    def print_misses_player_2(self):
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                if self.board_2[r][c] == HIT:
                    row.append(HIT)
                elif self.board_2[r][c] == MISS:
                    row.append(MISS)
                else:
                    row.append(WATER)
            print(" ".join(row))

    ########################################## PRINTING ##########################################

    def in_bounds(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def place_ships(self, player):
        board = self.board_1 if player == PLAYER_1 else self.board_2

        for length in self.ships:
            while True:
                try:
                    sr = int(input(f"Start row (length {length}): "))
                    sc = int(input(f"Start column (length {length}): "))
                    er = int(input(f"End row (length {length}): "))
                    ec = int(input(f"End column (length {length}): "))
                except ValueError:
                    print("Enter whole numbers.")
                    continue

                if not self.in_bounds(sr, sc) or not self.in_bounds(er, ec):
                    print("Coordinates not in bounds.")
                    continue

                if sr == er:
                    cells = [(sr, c) for c in range(min(sc, ec), max(sc, ec) + 1)]
                elif sc == ec:
                    cells = [(r, sc) for r in range(min(sr, er), max(sr, er) + 1)]
                else:
                    print("Ship must be horizontal or vertical.")
                    continue

                if len(cells) != length:
                    print("Wrong length.")
                    continue

                for r, c in cells:
                    board[r][c] = SHIP
                break

    def setup_ships(self):
        print(f"Player {PLAYER_1}, please place your ships")
        self.place_ships(PLAYER_1)
        print(f"Player {PLAYER_2}, please place your ships")
        self.place_ships(PLAYER_2)

    def game_over(self):
        pass

    def play(self):
        player, opponent = PLAYER_1, PLAYER_2
        board
        while not game_over():
            

            opponent, player = PLAYER_1, PLAYER_2







if __name__ == "__main__":
    answers = iter([
        "0", "0", "0", "1",   # player 1, length 2
        "2", "0", "2", "2",   # player 1, length 3
        "5", "0", "5", "1",   # player 2, length 2
        "7", "0", "7", "2",   # player 2, length 3
    ])

    with patch("builtins.input", lambda prompt="": next(answers)):
        game = Battleship(SHIP_LENGTHS)
        game.setup_ships()
        game.print_boards()
    

    game.play()

    print("------")
    game.print_player_1_full_board()
    print("------")
    game.print_player_2_full_board()


    # game = Battleship(SHIP_LENGTHS)
    # game.setup_ships()

    # game.print_boards()
    # print("------")
    # game.print_player_1_full_board()
    # print("------")
    # game.print_player_2_full_board()
    # print("------")
    # game.print_misses_player_1()
    # print("------")
    # game.print_misses_player_2()
    # print("------")

    # # game.play()
