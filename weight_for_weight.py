def weight_str(s):
    sum = 0
    for digit in s:
        sum += int(digit)
    return sum

def order_weight(strng):

    initial_list = sorted(strng.split())
    res = " ".join(sorted(initial_list, key=weight_str))

    return res

#print(order_weight("103 123 4444 99 101 101 2000"))
