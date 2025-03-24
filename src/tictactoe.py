X = True
O = False

WIN_SEQUENCES = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7)
)


class Move:
    def __init__(self, turn: bool, square: int):
        self.turn = turn
        self.square = square
    
    def __repr__(self):
        return f"Move({'X' if self.turn else 'O'}, {self.square})"


class Board:
    def __init__(self, turn: bool = X):
        self.first_turn = turn
        self.turn = turn
        self.grid = {
            1: None, 2: None, 3: None,
            4: None, 5: None, 6: None, 
            7: None, 8: None, 9: None
        }
        self.outcome = None
        self.move_stack = []
    

    def __str__(self):
        string = ""
        for square in self.grid:
            string += (("X" if self.grid[square] else "O") if self.grid[square] is not None else str(square))
            if square % 3 == 0: string += "\n"
            else: string += " "
        
        return string


    def switch_turn(self):
        self.turn = not self.turn
    

    def generate_possible_moves(self) -> list[Move]:
        moves = []

        if self.outcome is not None:
            return moves

        for square in self.grid:
            if self.grid[square] is None:
                move = Move(self.turn, square)
                moves.append(move)
        
        return moves
    

    def generate_empty_squares(self) -> list[int]:
        squares = []

        for square in self.grid:
            if self.grid[square] is None:
                squares.append(square)
        
        return squares


    def do_move(self, square: int):
        if self.outcome is not None:
            raise RuntimeError("Game has already finished.")

        if square not in self.grid:
            raise ValueError(f"Invalid square: {square}")
        
        if self.grid[square] is not None:
            raise ValueError(f"Square already occupied: {square}")
        
        move = Move(self.turn, square)
        self.grid[square] = self.turn
        self.move_stack.append(move)
        self._check_outcome()
        self.switch_turn()
    

    def undo_move(self) -> Move:
        if len(self.generate_possible_moves()) == 9:  # No move had been played
            raise RuntimeError("Can't undo move when no move has been made.")
    
        move = self.move_stack.pop()
        self.grid[move.square] = None
        self._check_outcome()
        self.switch_turn()

        return move


    def reset(self):
        self.turn = self.first_turn
        self.grid = {
            1: None, 2: None, 3: None,
            4: None, 5: None, 6: None, 
            7: None, 8: None, 9: None
        }
        self.outcome = None
        self.move_stack = []
    

    def _check_outcome(self):
        self.outcome = None

        if not self.generate_possible_moves():
            self.outcome = "DRAW"
            return
        
        for sequence in WIN_SEQUENCES:
            if self.grid[sequence[0]] == self.grid[sequence[1]] == self.grid[sequence[2]] != None:
                self.outcome = ("X" if self.move_stack[-1].turn else "O")
