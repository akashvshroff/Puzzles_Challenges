import math


def FastModularExponentiation(b, e, m):
    '''
    Function to find the modular exponentiation of b^e in a faster, more efficient method
    than multiplying 1 with b, e times.
    This represents e as either a square of 2 or a composite of the sums of the squares of 2 and then
    completes the exponentiation by squaring b the appropriate number of times.
    >>> FastModularExponentiation(7,13,11) #7^13 % 11
    2
    '''
    e_bin = bin(e)[2:]
    print(e_bin)
    if e_bin.count('1') == 1:  # Power of 2
        k = int(math.log2(e))
        c = b % m
        for i in range(0, k):
            c = (c * c) % m
        return c
    else:
        set_pos = []
        for i, l in enumerate(e_bin):
            if l == '1':
                set_pos.append(len(e_bin)-i-1)
        max_set = max(set_pos)
        c = b % m
        prod = []
        for i in range(max_set+1):
            if i in set_pos:
                prod.append(c)
            c = (c*c) % m
        product = 1
        for x in prod:
            product = (product * x) % m
        return product


# print(FastModularExponentiation(7, 13, 11))
