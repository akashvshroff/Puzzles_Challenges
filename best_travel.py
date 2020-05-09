from itertools import combinations

def choose_best_sum(t,k,ls):
    bs = 0 #best sum or closest sum to t
    cs = list(combinations(ls,k)) #list of possible combinations
    return max((sum(c) for c in cs if sum(c) <= t), default = None)

# xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# print(choose_best_sum(430, 5, xs))
