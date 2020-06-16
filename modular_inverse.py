def extended_euclid(n, a):
    if a == 0:
        return n, 1, 0
    d, p, q = extended_euclid(a, n % a)
    x = q
    y = p - (n//a)*q
    return d, x, y


def divide(a, b, n):
    '''
    Function to input 3 numbers a,b,n and return x such that b/a is congruent to
    x (mod n) i.e b is congruent to ax (mod n).
    '''
    gcd, t, s = extended_euclid(n, a)
    if s < 0:
        s = n + s
    assert (gcd == 1)  # if it has a multiplicative inverse
    return (b*s) % n


print(divide(5, 2, 6))
