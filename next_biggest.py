def next_bigger(n):
    """
    Given an integer, find the next permutation of it in absolute order.
    For example, given 48975, the next permutation would be 49578.

    If no such number exists, example given 4321, return the number itself.
    """
    digits = list(str(n))
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] > digits[i - 1]:
            digits[i], digits[i - 1] = digits[i - 1], digits[i]
            num = digits[:i]
            rem = sorted(digits[i:])
            return int(''.join(num+rem))
    return n


print(next_bigger(48975))
