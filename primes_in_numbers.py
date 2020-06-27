def find_prime_factors(num: int) -> list:
    '''
    Takes in any number and returns a list of its prime factors - the factors are
    repeated in case of multiple occurences as per their occurences.
    '''
    factors = []
    n = num
    while n % 2 == 0:
        n = n // 2
        factors.append(2)
    for i in range(3, int(n**0.5)+1, 2):
        while not n % i:
            n = n // i
            factors.append(i)
    if n > 2:
        factors.append(n)
    return factors if len(factors) > 1 else [num]


def primeFactors(n: int) -> str:
    """
    Factorize a number and find prime factors and return a str with factors.
    See also: https://www.codewars.com/kata/54d512e62a5e54c96200019e/solutions/python
    """
    res = ''
    factors = find_prime_factors(n)
    seen = []
    for fac in factors:
        if fac not in seen:
            n = factors.count(fac)
            if n > 1:
                res += '({}**{})'.format(fac, n)
            else:
                res += '({})'.format(fac)
            seen.append(fac)
    return res
