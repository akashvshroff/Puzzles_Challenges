def longest(s):
    """
    Return the longest alphabetical substring.
    Eg:
    >>> s = 'abshdbhsbaaaabbbbdddddad'
    >>> longest(s)
    "aaaabbbbddddd"
    """
    max_str, max_len = '', 0
    temp_str, temp_len = '', 0
    if len(s) <= 1:
        return s
    for i in range(len(s)):
        if not temp_str:
            temp_str, temp_len = s[i], 1
        else:
            if s[i] >= temp_str[-1]:
                temp_str += s[i]
                temp_len += 1
            else:
                if temp_len > max_len:
                    max_str, max_len = temp_str, temp_len
                temp_str, temp_len = s[i], 1
    return max(max_str, temp_str, key=len)


print(longest('abshdbhsbaaaabbbbdddddad'))
