cached = {}
def fibonacci(n):
    if n in cached.keys():
        return cached[n]
    if n in [0,1,2]:
       return 1
    value = fibonacci(n - 1) + fibonacci(n - 2)
    cached[n] = value
    return value
