def find_prime_factors(n: int) -> list:
    '''
    Takes in any number and returns a list of its prime factors - the factors are
    repeated in case of multiple occurences as per their occurences.
    '''
    if n <= 1:
        return ['Invalid']
    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append(2)
    for i in range(3, int(n**0.5)+1, 2):
        while not n % i:
            n = n // i
            factors.append(i)
    if n > 2:
        factors.append(n)
    return factors if len(factors) > 1 else ['Prime']


print(find_prime_factors(32))
