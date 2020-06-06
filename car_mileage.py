def is_sequence(num):
    fore = '1234567890'
    back = '9876543210'
    return True if str(num) in fore or str(num) in back else False


def check_interesting(num, awesome_phrases):
    if set(str(num)[1:]) == {'0'}:  # leading digit followed by 0
        return True
    if str(num) == str(num)[::-1]:  # palindrome or if only 1 num
        return True
    if awesome_phrases and num in awesome_phrases:
        return True
    if is_sequence(num):
        return True
    return False


def is_interesting(n, awesome_phrases):
    for i in range(n, n+3):
        if i >= 100:
            if check_interesting(i, awesome_phrases):
                if i == n:
                    return 2
                else:
                    return 1
    return 0


print(is_interesting(1336, [1337, 256]))
