def max_sequence(arr):
    max_sum, curr, max_seq, cur_seq = 0, 0, [], []
    for x in arr:
        curr += x
        cur_seq.append(x)
        if curr < 0:
            curr = 0
            cur_seq = []
        if curr > max_sum:
            max_sum = curr
            max_seq = cur_seq[::]
    return (max_sum, max_seq)


print(max_sequence([-3, 4, -4, 3, 2, 1, -4, 4, -1, 5, -6, -7]))
