import re


def solve_runes(runes):
    """
    Take in an expression with missing digits and return the smallest number that
    satisfies the equation.
    See also: https://www.codewars.com/kata/546d15cebed2e10334000ed9/train/python
    """
    if not runes.count('?'):
        return -1
    terms = re.split('\+|-|\*|=', runes)
    leading_num = False
    for term in terms:
        if '?' in term:
            if not term.index('?') and len(term) > 1:
                leading_num = True
                break
    for i in range(10):
        if str(i) in runes:
            continue
        if not i and leading_num:
            continue
        r_temp = runes.replace('?', str(i))
        exp1, exp2 = r_temp.split('=')
        if eval(exp1) == eval(exp2):
            return i
    return -1


print(solve_runes("?*11=??"))
