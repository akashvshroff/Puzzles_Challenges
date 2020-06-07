import math
import time

# the second method turns out to be faster than the sieve!


def find_primes_sieve(n):

    primes = []
    for i in range(2, n+1):
        primes.append(i)
    i = 2
    while (i <= int(math.sqrt(n))):
        if i in primes:
            for j in range(i*2, n+1, i):  # removes all the multiples of i
                if j in primes:
                    primes.remove(j)
        i += 1

    return primes


def find_primes(n):
    if n <= 1:
        return False
    if n == 2:
        return
    if n > 2 and n % 2 == 0:
        return False
    max_d = math.floor(math.sqrt(n))
    for i in range(3, max_d + 1, 2):
        if n % i == 0:
            return False
    return True


primes = []
start = time.time()
# find_primes_sieve(100000)
for i in range(1, 1000000):
    if find_primes(i):
        primes.append(i)

end = time.time()


print('Time taken for the function: {}'.format(end-start))
print(primes)
