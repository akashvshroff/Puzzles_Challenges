def next_smaller(n):
    a = list(str(n))
    r,l,f = [],[],[] #split into 2 lists, right, left, f for final list
    for i in range(len(a)-1,0,-1):
        if a[i]<a[i-1]:
            p = a[i-1]
            r = a[i:]
            l = a[:i-1]
            for j in range(len(r)-1,-1,-1):
                if r[j]<p:
                    r[j],p = p, r[j]
                    r = sorted(r, reverse = True)
                    f = l + list(p) + r
                    if f[0] == '0':
                        return -1
                    else:
                        return int(''.join(f))
    return -1

#print(next_smaller(1027))
