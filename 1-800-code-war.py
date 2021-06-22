import itertools as it


def get_possibilities(comps, letter_dict, words_dict):
    comp_poss = []
    for comp in comps:
        poss = []
        for letter in comp:
            poss.append(letter_dict[letter])
        poss_words = list(it.product(*poss))
        temp = []
        for word_tuple in poss_words:
            word = ''.join(word_tuple)
            if words_dict.get(word, False):
                temp.append(word)
        comp_poss.append(temp)
    comp_poss = list(it.product(*comp_poss))
    possibilities = {'1-800-{}-{}'.format(*poss) for poss in comp_poss}
    return possibilities


def check1800(s):
    letter_dict = {
        'A': 'ABC',
        'B': 'ABC',
        'C': 'ABC',
        'D': 'DEF',
        'E': 'DEF',
        'F': 'DEF',
        'G': 'GHI',
        'H': 'GHI',
        'I': 'GHI',
        'J': 'JKL',
        'K': 'JKL',
        'L': 'JKL',
        'M': 'MNO',
        'N': 'MNO',
        'O': 'MNO',
        'P': 'PQRS',
        'S': 'PQRS',
        'Q': 'PQRS',
        'R': 'PQRS',
        'T': 'TUV',
        'U': 'TUV',
        'V': 'TUV',
        'W': 'WXYZ',
        'X': 'WXYZ',
        'Y': 'WXYZ',
        'Z': 'WXYZ'
    }
    words_dict = {word: True for word in WORDS}  # WORDS is a preloaded list
    comps = s.split('-')[2:]
    poss1 = get_possibilities(comps, letter_dict, words_dict)
    if len(comps[0]) == 3:
        comps = [comps[0]+comps[1][0], comps[1][1:]]
    else:
        comps = [comps[0][:-1], comps[0][-1]+comps[1]]
    poss2 = get_possibilities(comps, letter_dict, words_dict)
    return poss1.union(poss2)
