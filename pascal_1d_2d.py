def pascal(n):
    arr = [[0 for x in range(n)]
               for y in range(n)]
    fin = []
    for r in range(0,n):
        for c in range(0,r+1):
            if c == 0 or c == r:
                arr[r][c]=1
                fin.append(1)
            else:
                arr[r][c]=arr[r-1][c-1]+arr[r-1][c]
                fin.append(arr[r][c])
    return fin
#pascal(5)
