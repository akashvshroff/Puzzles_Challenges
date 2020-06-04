def count_set_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count


def check_pow_2(n):
    if count_set_bits(n) == 1:
        return True
    else:
        return False


print(check_pow_2(16))
