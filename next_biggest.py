def next_bigger(n):
    a = list(str((n)))
    r,l,f = [],[],[]
    for i in range(len(a)-1,0,-1):
        if a[i]>a[i-1]:
           p = a[i-1]
           r = a[i:]
           l = a[:i-1]
           for j in range(len(r)-1,-1,-1):
                if r[j]>p:
                    r[j],p = p,r[j]
                    r = sorted(r)
                    f = l + list(p) + r
                    return int(''.join(f))
    return -1
