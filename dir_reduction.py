def dirReduc(arr):
    dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    r = []
    for i in arr:
        if r and dict[i] == r[-1]:
            r.pop()
        else:
            r.append(i)
    return r
