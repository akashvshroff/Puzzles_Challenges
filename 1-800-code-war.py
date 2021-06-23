import itertools as it
from collections import defaultdict


def check1800(s):
    """
    Given the 1-800 (phone word) number that the company wants to use,
    you need to check against all known words and return the set of all possible 1-800 numbers
    which can be formed using those same digits.

    There is a preloaded array of lots of 3 and 4 letter (upper-case) words:
    For Python it is: WORDS

    Link: https://www.codewars.com/kata/5a3267b2ee1aaead3d000037/train/python
    """
    num_translation = str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '22233344455566677778889999')
    nums_dict = defaultdict(list)
    for word in WORDS:
        nums_dict[word.translate(num_translation)].append(word)

    number = s[6:].replace('-', '').translate(num_translation)

    # we take the cartesian product of all the options for the first word and all the options for the second.

    # case 1, first word is 3 letter & second is 4 letter
    possibilities1 = {'1-800-{}-{}'.format(*poss) for poss in it.product(
        nums_dict[number[:3]], nums_dict[number[3:]])}

    # case 2, first word is 4 letter & second is 3 letter
    possibilities2 = {'1-800-{}-{}'.format(*poss) for poss in it.product(
        nums_dict[number[:4]], nums_dict[number[4:]])}

    return possibilities1.union(possibilities2)
