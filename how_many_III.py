from itertools import combinations_with_replacement
def find_all(sum_dig, digs):
    fin = []
    ds = list(combinations_with_replacement('123456789',digs))
    for d in ds:
        s = 0
        for l in d:
            s += int(l)

        if s == sum_dig:
            fin.append(int(''.join(d)))
    if fin:
        return [len(fin), fin[0], fin[-1]]
    else:
        return []
