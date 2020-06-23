def scramble(s1, s2):
    """
    A function to see if a substring of s1 can be scrambled to make s2.
    See also: codewars.com/kata/55c04b4cc56a697bb0000048/train/python
    One-liner: return all(s1.count(l) >= s2.count(l) for l in set(s2))
    """
    for l in set(s2):
        if not s1.count(l) >= s2.count(l):
            return False
    return True
