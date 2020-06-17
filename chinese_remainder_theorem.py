def ext_euclid(n1, n2):  # n2 must be lesser than n1
    if n2 == 0:
        return n1, 1, 0
    gcd, p, q = ext_euclid(n2, n1 % n2)
    x = q
    y = p - (n1//n2)*q
    return gcd, x, y


def chinese_remainder(n1, r1, n2, r2):
    '''
    The function takes in 2 co-prime numbers and the remainders that a possible number n
    is congruent to mod the respective numbers. i.e n is congruent to r1 (mod n1)
    and so on.
    Therefore using euclid's extended algorithm, we can determine n1x + n1y = 0.
    Hence using this, we can find n for the product of remainders mod(n1*n2). Hence we return n % (n1*n2).
    '''
    swapped = False
    if not n1 >= n2:
        swapped = True
        n1, n2 = n2, n1
    d, x, y = ext_euclid(n1, n2)
    ax, by = 0, 0
    if swapped:
        ax = n2*y
        by = n1*x
    else:
        ax, by = n1*x, n2*y
    n = r1*by + r2*ax
    return n % (n1*n2)


print(chinese_remainder(686579304, 295310485, 26855093, 8217207))
