from collections import defaultdict


def recoverSecret(triplets: list) -> str:
    '''
    Recovers a secret message from a list of random substrings (len 3) where order in the substring is the
    order in the secret string.
    For example, [['w','h','i']] would be a valid substring for the string 'whatisup'.
    '''


triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]
recoverSecret(triplets)
