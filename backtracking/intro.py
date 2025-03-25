"""
Back tracking

Write a simple backtracking algorithm
to solve the N-Queens problem.

The N-Queens problem is to place N queens on an N×N chessboard
such that no two queens can attack each other.
The goal is to find all possible solutions.

For example, with N = 4, there are 2 solutions:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""
def solveNQueens(n):
    def backtrack(row, cols, diag1, diag2):
        if row == n:
            solutions.append(["." * i + "Q" + "." * (n - i - 1) for i in cols])
        else:
            for col in range(n):
                if col not in cols and row + col not in diag1 and row - col not in diag2:
                    backtrack(row + 1, cols + [col], diag1 + [row + col], diag2 + [row - col])

    solutions = []
    backtrack(0, [], [], [])
    return solutions

# Example usage:
solutions = solveNQueens(4)
for solution in solutions:
    for row in solution:
        print(row)
    print()