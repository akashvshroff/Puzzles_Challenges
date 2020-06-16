def extended_euclid(a, b):
    if b == 0:
        d, x, y, = a, 1, 0
    else:
        d, p, q = extended_euclid(b, a % b)
        x = q
        y = p - q * (a//b)
    return (d, x, y)


def diophantine(a, b, c):
    '''
    A means to solve diophantine equations using extended euclidian algorithm.
    Diophantine Equations are polynomial equations that have integer solutions - eg. 3x + 5y = 22
    and are extremely helpful in solving real world issues. The fn returns x and y.
    '''
    swapped = False
    if not a >= b:
        a, b = b, a
        swapped = True
    d, p, q = extended_euclid(a, b)
    factor = c//d
    return (p*factor, q*factor) if not swapped else (q*factor, p*factor)


print(ext_gcd(10, 6))
