def longest_consec(strarr, k):
    """
    Longest consecutive string of terms lenght k from an array of string.
    """
    if not strarr or k <= 0 or k > len(strarr):
        return ''
    elif k == 1:
        return max(strarr, key=len)
    elif k == len(strarr):
        return ''.join(strarr)
    else:
        curr_max = ''
        for i in range(0, len(strarr)-k+1, 1):
            sub_string = ''.join(strarr[i:i+k])
            if not curr_max:
                curr_max = sub_string
            elif curr_max and len(sub_string) > len(curr_max):
                curr_max = sub_string
        return curr_max
