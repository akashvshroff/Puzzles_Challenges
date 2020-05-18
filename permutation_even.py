def is_even(p):
    n = 0
    for i in range(1, len(p)):
        key = p[i]
        j = i - 1
        while j >= 0:
            if p[j] > key:
                n += 1
                p[j + 1], p[j] = p[j], key
            j -= 1
    return True if n % 2 == 0 else False


print(is_even([[0, 3, 2, 4, 5, 6, 7, 1, 9, 8]]))
