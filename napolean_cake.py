def layers(n, a):
    cake = []
    c = a[n-1]
    for i in range(n - 1, -1, -1):
        if a[i] >= c:
            c = a[i]
        if c > 0 and c >= a[i]:
            cake.append('1')
            c -= 1
        else:
            cake.append('0')
    return reversed(cake)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = layers(n, a)
    print(' '.join(ans))
