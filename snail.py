def calculate_next(r,c,d):
    if d == 'right':
        return r,c+1
    elif d == 'down':
        return r+1,c
    elif d == 'left':
        return r,c-1
    else:
        return r-1,c

def is_valid(r,c,s,n):
    if not 0 <= r < n:
        return False
    if not 0 <= c < n:
        return False
    if [r,c] in s:
        return False
    return True


def snail(snail_map):
    '''
    Traverse a n*n matrix in a snail, clockwise pattern.
    https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python

    >>> array = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
    >>> print(snail(array))
    [1,2,3,6,9,8,7,4,5]
    
    '''
    n = len(snail_map)
    dirs = {'right':'down','down':'left','left':'up','up':'right'}
    curr_dir = 'right'
    curr_row,curr_col,next_row,next_col = 0,0,None,None
    seen = [[0,0]]
    res = [snail_map[curr_row][curr_col]]
    while len(seen) < n*n:
        next_row,next_col = calculate_next(curr_row,curr_col,curr_dir)
        if is_valid(next_row,next_col,seen,n):
            curr_row,curr_col = next_row,next_col
            res.append(snail_map[curr_row][curr_col])
            seen.append([curr_row,curr_col])
        else:
            curr_dir = dirs[curr_dir]
    return res
