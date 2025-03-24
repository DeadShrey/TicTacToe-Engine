import tictactoe
import os
import platform


def clear(): 
    os.system("cls") if platform.system() == "Windows" else os.system("clear")


board = tictactoe.Board()
while board.outcome is None:
    print(board, "\n")
    square = input(f"{"X" if board.turn else "O"} > ")
    clear()

    if not square.isnumeric():
        print(f"Invalid square: {square}", "\n")
        continue
    
    if int(square) not in board.generate_empty_squares():
        print(f"Invalid move: {square}", "\n")
        continue

    board.do_move(int(square))


if board.outcome == "DRAW": print("The game was a draw.")
else: print(f"{board.outcome} won the game!")
print("\n", board)
