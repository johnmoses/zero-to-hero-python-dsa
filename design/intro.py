""" 
Design algorithms
Design tic-tac-toe
"""
def initialize_board():
    """Create empty 3x3 board"""
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    """Display the current board state"""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_winner(board, player):
    """Check if the given player has won"""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    """Check if the board is full (tie)"""
    return all(board[i][j] != " " for i in range(3) for j in range(3))
