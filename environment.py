from enum import Enum
import random

class Piece(Enum):
    O = 0
    X = 1
    EMPTY = -99999

class Condition(Enum):
    O_Won = 1
    X_Won = -1
    TIE = 0
    CONTINUE = 9999

# Define the game environment
class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[Piece.EMPTY for _ in range(size)] for _ in range(size)]

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
        return self.check_condition_board()
    
    # check if there is a tie or win for either pieces
    def check_condition_board(self):
        # check all rows first 
        for i in range(self.size):
            if sum([piece.value for piece in self.board[i]]) == 3:
                return Condition.O_Won
            if sum([piece.value for piece in self.board[i]]) == 0:
                return Condition.X_Won
        
        # check all cols
        for i in range(self.size):
            curr_sum = 0
            for j in range(self.size):
                curr_sum += self.board[j][i].value
            
            if curr_sum == 3:
                return Condition.O_Won
            if curr_sum == 0:
                return Condition.X_Won
        
        # check the two diagnols

        # from (0,0) to (size-1,size-1)
        i = 0
        j = 0
        curr_sum = 0
        while i < self.size:
            while j < self.size:
                curr_sum += self.board[i][j].value
                i+=1
                j+=1

        if curr_sum == 3:
            return Condition.O_Won
        if curr_sum == 0:
            return Condition.X_Won
        
        # from (0,0) to (size-1,size-1)
        i = self.size - 1
        j = 0
        curr_sum = 0
        while i >= 0:
            while j < self.size:
                curr_sum += self.board[i][j].value
                i-=1
                j+=1

        if curr_sum == 3:
            return Condition.O_Won
        if curr_sum == 0:
            return Condition.X_Won
        
        # It's a TIE if there aren't any available spots
        if not self.available_spots:
            return Condition.TIE
        
        # if there are available spots but no win/lose condition 
        # then we have to continue
        return Condition.CONTINUE
          
    def get_available_spots(self):
        return self.available_spots

    def get_board(self):
        return self.board
    
    def __repr__(self):
        return "Board: size = %d\n%s" % (self.size, self.board)
    

# Define RL Agent

# Agent will randomly place a piece anywhere on the board
class RandomAgent:
    def __init__(self, board, piece):
        self.board = board
        self.total_games = 0
        self.wins = 0
        self.piece = piece
        
    
    def move(self):
        if not self.board.get_available_spots():
            raise ValueError("No available spots")
        
        available_spots = self.board.get_available_spots()
        
        random_x, random_y = random.choices(list(available_spots), k=1)[0]
        condition = self.board.add_piece(random_x, random_y)


        if condition == Condition.TIE or Condition.O_Won or Condition.X_Won:
            self.total_games+=1
        
        if self.piece == Piece.O:
            if condition == Condition.O_Won:
                self.wins+=1
        elif self.piece == Piece.X:
            if condition == Condition.O_Won:
                self.wins+=1

        return condition

class SmarterAgent:
    def __init__(self, board, piece):
        self.board = board
        self.total_games = 0
        self.wins = 0
        self.piece = piece

    
    



board = Board(3)
O_agent = RandomAgent(board, Piece.O)
X_agent = RandomAgent(board, Piece.X)


condition = Condition.CONTINUE





