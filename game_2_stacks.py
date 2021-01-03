def two_stacks(x, a, b):
    """
    Given a maximum limit and 2 stacks where in each turn you can remove the top
    element from each stack with the aim of removing the most elements while remaining
    under the limit.

    x = 10
    a = 4 2 4 6 1
    b = 2 1 8 5

    max score = 4
    """
    total, score = 0, 0

    for num in a:
        if total + num <= x:
            score += 1
            total += num
        else:
            break
    max_score = score
    counter = 0
    for num in b:
        total += num
        score += 1
        while total > x and counter < len(a):
            total -= a[counter]
            counter += 1
            score -= 1
        if total <= x and max_score < score:
            max_score = score
    return max_score


x = 10
a = [4, 2, 4, 6, 1]
b = [2, 1, 8, 5]

print(two_stacks(x, a, b))
