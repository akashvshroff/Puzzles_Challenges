def max_sequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:
            curr=0
        if curr>max:
            max=curr
    return max

#print(max_sequence([-3,4,-4,3,2,1,-4,4,-1,5,-6,-7]))
