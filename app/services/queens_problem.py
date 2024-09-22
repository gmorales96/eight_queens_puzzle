def validate(chessboard, row, col):
    # Check if there's a queen in the same column
    for i in range(row):
        if chessboard[i] == col:
            return False

    # Check diagonal (\ direction)
    for i in range(row):
        if chessboard[i] - i == col - row:
            return False

    # Check diagonal (/ direction)
    for i in range(row):
        if chessboard[i] + i == col + row:
            return False

    # If no conflicts, the position is valid
    return True

def get_solutions(chessboard, row, solutions):
    # If we've placed queens in all rows, add the solution to the list
    if row == len(chessboard):
        solutions.append(chessboard.copy())
        return

    # Try placing a queen in each column of the current row
    for col in range(len(chessboard)):
        if validate(chessboard, row, col):
            chessboard[row] = col
            get_solutions(chessboard, row + 1, solutions)
            chessboard[row] = -1

    return solutions

def queens(n):
    chessboard = [-1] * n
    solutions = get_solutions(chessboard, 0, [])

    # Return all valid solutions for the n-queens problem
    return solutions
