def solve(n):
    """
    Given an integer n, find the largest integer smaller than (or including n)
    that has the maximum sum of its digits.
    Eg.:
    >>> solve(48)
    48
    >>> solve(100)
    99
    0<=n<=1e11
    """
    if not n:
        return 0
    max_sum = float("-inf")
    num = None
    for i in range(n, 0, -1):
        curr_sum = sum(map(int, str(i)))
        if curr_sum > max_sum:
            num = i
            max_sum = curr_sum
    return num


print(solve(1009))
