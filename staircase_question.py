def solve_staircase(n):
    """
    There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
    Given N, write a function that returns the number of unique ways you can climb the staircase.
    The order of the steps matters.
    See also: https://www.dailycodingproblem.com/blog/staircase-problem/
    """
    a, b = 1, 2
    for _ in range(n-1):  # just a modification on the fibonacci seq.
        a, b = b, a+b
    return a


def solve_staircase_input(n, steps):
    """
    The same as above but now the number of steps you can take are user inputs.
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in steps:
        return 1 + sum(solve_staircase_input(n - x, steps) for x in steps if x < n)
    else:
        return sum(solve_staircase_input(n - x, steps) for x in steps if x < n)


def staircase_input_faster(n, steps):
    """
    Had to refer to the solution for this!
    """
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in steps if i - x > 0)
        cache[i] += 1 if i in steps else 0
    return cache[-1]


print(staircase_input_faster(25, [1, 2, 3]))
