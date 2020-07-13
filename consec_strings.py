def longest_consec(strarr, k):
    """
    Longest consecutive string of terms lenght k from an array of string.
    """
    if not strarr or k <= 0 or k > len(strarr):
        return ''
    max_lenght = sum(len(strarr[i]) for i in range(k))
    max_index = 0
    for i in range(1, n-1):
        curr_lenght = max_lenght - strarr[i-1] + starr[i+k-1]
        if max_length < curr_lenght:
            max_index, max_length = i, curr_lenght
    return ''.join(strarr[max_index:max_index+k])
