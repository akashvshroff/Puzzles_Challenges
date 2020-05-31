import string
from operator import itemgetter


def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=itemgetter(key), reverse=reverse)
    return xs


def mix(s1, s2):
    string_list, res = [], ''
    for l in string.ascii_lowercase:
        c1, c2, num = s1.count(l), s2.count(l), 0
        if c1 != c2:
            key, num = ('1', c1) if c1 > c2 else ('2', c2)
        else:
            key, num = '3', c1
        if num <= 1:
            continue
        string_list.append((key, l*num, num))
    string_fin = multisort(list(string_list), ((2, True), (0, False), (1, False)))
    for k, l, _ in string_fin:
        if k == '3':
            k = '='
        res += '{}:{}/'.format(k, l)
    return res[:-1]


# "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
mix("looping is fun but dangerous", "less dangerous than coding")
