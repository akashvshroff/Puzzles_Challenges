import numpy as np


class Sudoku(object):
    """
    A class to check if a sudoku of size n*n is valid, where n**0.5, i.e root n
    is an integer and forms the smaller grid. Acceptable numbers are from 1 to n
    and the standard rules of a sudoku puzzle apply.
    """

    def __init__(self, data):
        self.board = data
        self.n = len(self.board)
        self.mini_n = int(self.n**0.5)
        self.is_valid()

    def is_valid(self):
        for row in self.board:
            for col in row:
                if type(col) != type(self.n):
                    return False
        acceptable = [i for i in range(1, self.n+1)]
        grid = np.transpose(self.board)
        if np.count_nonzero(grid == 0):
            return False
        for row in self.board:
            if sorted(row) != acceptable:
                return False
        for row in grid:
            if not sorted(row) == acceptable:
                return False
        for row in range(0, self.n, self.mini_n):
            for col in range(0, self.n, self.mini_n):
                temp = []
                for r in range(row, row+self.mini_n):
                    for c in range(col, col + self.mini_n):
                        temp.append(self.board[r][c])
                if sorted(temp) != acceptable or len(temp) != len(set(temp)):
                    return False
        return True


#
goodSudoku2 = Sudoku([
    [True, False],
    [False, True]
])


print(type(52) == type(20))
