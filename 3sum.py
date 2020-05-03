import itertools
def three(arr, sum):
    sol = []
    arr = sorted(arr)
    for i in range(len(arr)-2):
        l = i+1
        r = len(arr)-1
        while l < r:
            s = arr[i]+arr[l]+arr[r]
            if s == sum:
                sol.append([arr[i],arr[l],arr[r]])
                l = l+1
                r = r-1
            elif s < sum:
                l += 1
            elif s > sum:
                r -= 1
    sol.sort()
    return [k for k in itertools.groupby(sol)]


#print(three([2,0,3,-1,3,2,-1,-3,2,0,1],0))
