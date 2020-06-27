def encrypt_this(text):
    """
    Encrypt a string such that the first character is converted to its ASCII
    value and the second and last characters are swapped.
    See also: https://www.codewars.com/kata/5848565e273af816fb000449/train/python
    """
    res = " "
    for word in text.split():
        word = list(word)
        word[0] = str(ord(word[0]))
        if len(word) > 2:
            word = word[0] + word[-1] + ''.join(word[2:-1]) + word[1]
        res += ''.join(word) + ' '
    return res.strip()


print(encrypt_this('hi there this is mne'))
