from enum import Enum

class Piece(Enum):
    O = 0
    X = 1

class Condition(Enum):
    O_Won = 1
    X_Won = -1
    TIE = 0

# Define the game environment
class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[-1 for _ in range(size)] for _ in range(size)]

        # set of tuples to check available spots
        self.available_spots = {
            (i, j) for i in range(size) for j in range(size)
        }

        # O starts first
        self.curr_piece_turn = Piece.O

    def add_piece(self, x, y):
        # Add the piece to the board
        
        if (x,y) not in self.available_spots:
            raise ValueError(f"(x,y) is incorrect")
        
        self.board[x][y] = self.curr_piece_turn
        self.curr_piece_turn = Piece.X if self.curr_piece_turn == Piece.O else Piece.O
        self.available_spots.remove((x,y))

    def inspect_board(self):
        # Return a list of all pieces on the board
        pieces = []
        for y in range(self.size):
            for x in range(self.size):
                if self.board[y][x] == 1:
                    pieces.append((y, x))
        return pieces
    
    def check_condition_board(self):
        pass
    
    def get_available_spots(self):
        return self.available_spots

    def get_board(self):
        return self.board
    
    def __repr__(self):
        return "Board: size = %d\n%s" % (self.size, self.board)


board = Board(3)
