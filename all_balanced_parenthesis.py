import itertools as it

perms = list(it.permutations('()()'))
for perm in perms:
    print(''.join(perm))
