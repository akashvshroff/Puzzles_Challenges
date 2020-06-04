def check_num(n):
    if n % 10 == 0:
        return False
    rev = int(str(n)[::-1])
    if n == rev:
        return False
    return True if not (rev+n) % abs(rev - n) else False


def sum_dif_rev(n):
    cached = []
    if not n:
        return 0
    i = 45
    nums = []
    while len(nums) < n:
        if i in cached:
            nums.append(i)
        elif check_num(i):
            cached.append(int(str(i)[::-1]))
            nums.append(i)
        i += 9

    return nums[-1]


print(sum_dif_rev(65))
