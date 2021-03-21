def min_ops(n, k, s):
    """
    Charles defines the goodness score of a string as the number of indices
    i such that Si≠SN−i+1 where 1≤i≤N/2 (1-indexed). For example, the string
    CABABC has a goodness score of 2 since S2≠S5 and S3≠S4.

    Charles gave Ada a string S of length N, consisting of uppercase letters
    and asked her to convert it into a string with a goodness score of K. In one
    operation, Ada can change any character in the string to any uppercase letter.
    Could you help Ada find the minimum number of operations required to transform
    the given string into a string with goodness score equal to K?
    """
    score = 0
    limit = n//2
    for i in range(n):
        if i < limit and s[i] != s[n-i-1]:
            score += 1
    if score == k:
        return 0
    else:
        return abs(k - score)


if __name__ == '__main__':
    test = int(input())
    for t in range(test):
        n, k = map(int, input().split())
        s = input()
        ans = min_ops(n, k, s)
        print(f'Case #{t+1}: {ans}')
