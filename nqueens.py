import numpy as np


def is_valid(board, row, col, n):
    if board[row][col] == 1:
        return False

    if 1 in np.transpose(board)[col]:
        return False

    x, y = row, col
    while (x >= 0 and y >= 0):  # left diagonal
        if (board[x][y] == 1):
            return False
        x -= 1
        y -= 1

    x, y = row, col
    while (x >= 0 and y < n):  # right diagonal
        if (board[x][y] == 1):
            return False
        x -= 1
        y += 1

    return True


def solve_board(board, n, row):
    if row == n:  # base case
        print('-'*n)
        for row in board:
            for col in row:
                if col == 1:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print("")
        return

    else:
        for col in range(n):
            if (is_valid(board, row, col, n)):
                board[row][col] = 1
                solve_board(board, n, row=row + 1)
                board[row][col] = 0
        return False


def main():
    n = 4
    board = np.zeros((n, n), dtype=int)
    solve_board(board, n, 0)


main()
