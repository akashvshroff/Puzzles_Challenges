def josephus_permutation(n, k):
    res = 0
    # since formula for josephus with index 0 is Jn,k = (J(n-1),k + k )%n
    for i in range(1, n+1):
        res = (res + k) % i

    return res+1
