cached = {}


def fibonacci(n):
    if n in cached.keys():
        return cached[n]
    if n in [0, 1, 2]:
        return 1
    value = fibonacci(n - 1) + fibonacci(n - 2)
    cached[n] = value
    return value


def fibonacci_iter(n):
    # iterative
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b


print(fibonacci_iter(10))
