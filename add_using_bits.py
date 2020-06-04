def add_nums(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


print(add_nums(5, 3))
