def middle_permutation(string):
    string = ''.join(sorted(string))
    if not len(string) % 2:
        middle = string[len(string)//2-1]
        remaining = [l for l in string if l != middle][::-1]
        return middle + ''.join(remaining)
    else:
        mid = string[len(string)//2]
        remaining = [l for l in string if l != mid]
        res = middle_permutation(''.join(remaining))
        return mid + res


print(middle_permutation('abcd'))
