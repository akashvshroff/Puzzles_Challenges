import time


def euclid_gcd(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def euclid_recursive(a, b):  # only if a >= b so wrapped
    return euclid_recursive(b, a % b) if b > 0 else a


def euclid_wrapper(fn):  # wraps recursive so it can swap the numbers
    def inner(a, b):
        a, b = (a, b) if a >= b else (b, a)
        return fn(a, b)
    return inner


def naive_gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    for d in range(min(a, b), 0, -1):
        if not a % d and not b % d:
            return d
    return 1


def extended_euclid(a, b):  # again wrapped
    # if a%d and b%d == 0, and d = xa + yb then d = gcd(a,b)
    # again for a >= b
    if b == 0:
        d, x, y, = a, 1, 0
    else:
        d, p, q = extended_euclid(b, a % b)
        x = q
        y = p - q * (a//b)
    return (d, x, y)


a, b = 1000000001, 4561233283

# st_naive = time.time()
# naive_gcd(a,b)
# end_naive = time.time()
# print('The naive algorithm took {} seconds.'.format(end_naive-st_naive))
# The naive algorithm took 60.2246994972229 seconds.

st_euclid = time.time()
# wrapped_rec = euclid_wrapper(euclid_recursive)
# wrapped_ext = euclid_wrapper(extended_euclid)
# print(wrapped_rec(a,b))
# print(wrapped_ext(a,b))
print(euclid_gcd(a, b))
end_euclid = time.time()
print('The euclid algorithm took {} seconds.'.format(end_euclid-st_euclid))
# The euclid algorithm took 0.0 seconds.
