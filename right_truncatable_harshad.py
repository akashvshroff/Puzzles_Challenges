def get_sum(n):
    sum = 0
    while(n > 0):
        sum += int(n % 10)
        n = int(n/10)
    return sum


def is_harshad(n):
    while n >= 1:
        if n % get_sum(n) == 0:
            n = n//10
            is_harshad(n)
        else:
            return False
    return True


def rthn_between(a, b):
    rthn = []
    for i in range(a, b+1):
        if i < 10:
            continue
        if is_harshad(i):
            rthn.append(i)
    return rthn


#print(rthn_between(30, 1000000))
