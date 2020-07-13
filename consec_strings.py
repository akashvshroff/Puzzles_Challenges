def longest_consec(strarr, k):
    """
    Longest consecutive string of terms lenght k from an array of string.
    """
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''

    length = sum(len(strarr[i]) for i in range(k))
    max_length = length
    max_index = 0
    for index in range(0, n - k):
        length += len(strarr[index + k]) - len(strarr[index])
        if length > max_length:
            max_length, max_index = length, index + 1

    return ''.join(strarr[max_index:max_index + k])
