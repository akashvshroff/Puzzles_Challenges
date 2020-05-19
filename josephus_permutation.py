def josephus_permutation(items, k):
    index = -1
    res = []
    while len(items) > 1:
        # print(items)
        index = (index + k) % len(items)
        gone = items.pop(index)
        res.append(gone)
        index -= 1
    return res + items


print(josephus_permutation([1, 2, 3, 4, 5, 6, 7], 3))
