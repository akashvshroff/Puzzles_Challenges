def solve(arr):
    """
    You are given 3 piles of casino chips and each day you can pick up 2 but
    of different colours. How many days will it last?
    eg. arr = 4,1,1
    >>> 2
    See also:
    https://www.codewars.com/kata/5e0b72d2d772160011133654/train/python
    """
    a, b, c = sorted(arr)
    return min(a+b, (a+b+c)//2)


print(solve([7, 4, 8]))
