import tictactoe


searched_positions = 0


def search(board: tictactoe.Board):
    if board.outcome is not None:
        global searched_positions
        searched_positions += 1

        if board.outcome == "DRAW": return 0
        elif board.outcome in "OX": return -1
        else: raise LookupError("Somehow a weird outcome emerged.")
    
    best_score = -float("inf")
    for move in board.generate_possible_moves():
        board.do_move(move.square)
        score = -search(board)
        board.undo_move()
        best_score = max(best_score, score)

    return best_score


def generate_best_move(board: tictactoe.Board):
    best_score = -float("inf")
    best_move = None
    global searched_positions
    searched_positions = 0

    for move in board.generate_possible_moves():
        board.do_move(move.square)
        score = -search(board)
        board.undo_move()
        
        if score >= best_score:
            best_score = score
            best_move = move

    return best_move
