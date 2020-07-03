import string


def vertical_histogram_of(s):
    """
    Display a vertical histogram of occurences of uppercase letters in strings.
    See also: https://www.codewars.com/kata/59cf0ba5d751dffef300001f
    """
    letter_count = {letter: s.count(letter) for letter in string.ascii_uppercase if letter in s}
    hist = ""
    if not letter_count:
        return hist
    letters = letter_count.keys()
    i_max = max(letter_count.values())
    while i_max > 0:
        row = ['*' if letter_count[letter] >= i_max else ' ' for letter in letters]
        hist += ' '.join(row).rstrip() + '\n'
        i_max -= 1
    hist += ' '.join(letters).rstrip()
    return hist
