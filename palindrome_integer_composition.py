def values(n):
    """
    Find the count of numbers less than n that are palindromic and can be
    represented as the sum of consecutive squares - eg. 595 which is a
    palindrome and is 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.
    See also:
    - Project Euler 125
    - https://www.codewars.com/kata/599b1a4a3c5292b4cc0000d5/train/python
    """
    squares = {}
    res = set()
    lim = int(n**0.5)
    for i in range(1, n):
        if i in squares:
            sos = squares[i]
        else:
            sos = i*i
            squares[i] = sos
        while sos < n:
            i += 1
            sq = 0
            if i in squares:
                sq = squares[i]
            else:
                sq = i*i
                squares[i] = sq
            sos += sq
            if sos < n and str(sos) == str(sos)[::-1]:
                res.add(sos)
    return len(res)


print(values(100))
