import math


def find_primes(num):
    primes = []
    for n in range(num+1):
        found = True
        if n <= 1:
            continue
        if n == 2:
            primes.append(n)
            continue
        if n > 2 and n % 2 == 0:
            continue
        max_d = math.floor(math.sqrt(n))
        for i in range(3, max_d + 1, 2):
            if n % i == 0:
                found = False
                break
        if found:
            primes.append(n)
    return primes


def proper_fractions(n):
    if n <= 1:
        return 0
    num = int(math.sqrt(n))
    primes = find_primes(num)
    phi = 1
    m = n
    for prime in primes:
        if not m % prime:
            phi *= (prime-1)
            m //= prime
        while not m % prime:
            phi *= prime
            m //= prime
    if m > 1:
        phi *= (m-1)
    return phi + 1  # to account for the one


print(proper_fractions(10))
