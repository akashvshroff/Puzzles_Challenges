import numpy as np

def valid_solution(board):

    y = np.array(board) #check full board
    if np.count_nonzero(y==0) != 0:
        return False

    for row in board: #check rows
        if sorted(row) != [1,2,3,4,5,6,7,8,9]:
            return False

    y1 = np.transpose(board)
    for row in y1: #check columns
        if sorted(row) != [1,2,3,4,5,6,7,8,9]:
            return False

    for row in range(0, 9, 3):
          for col in range (0,9,3):
             temp = []
             for r in range (row,row+3):
                for c in range (col, col+3):
                    temp.append(board[r][c])
             #print(temp)
             if any(i < 0 and i > 9 for i in temp):
                 return False
             elif len(temp) != len(set(temp)):
                 return False

    return True


# board =  [[5, 3, 4, 6, 7, 8, 9, 1, 2],
#           [6, 7, 2, 1, 9, 0, 3, 4, 8],
#           [1, 0, 0, 3, 4, 2, 5, 6, 0],
#           [8, 5, 9, 7, 6, 1, 0, 2, 0],
#           [4, 2, 6, 8, 5, 3, 7, 9, 1],
#           [7, 1, 3, 9, 2, 4, 8, 5, 6],
#           [9, 0, 1, 5, 3, 7, 2, 1, 4],
#           [2, 8, 7, 4, 1, 9, 6, 3, 5],
#           [3, 0, 0, 4, 8, 1, 1, 7, 9]]
