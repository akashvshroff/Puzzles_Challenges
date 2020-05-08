def best_match(goals1,goals2):
    gd,zg,r = None,0,0
    for i,(x,y) in enumerate(zip(goals1,goals2)):
        if not gd:
            gd,zg,r = x - y,y,i
        else:
            if x - y < gd:
                gd,zg,r = x - y,y,i
            elif x - y == gd:
                if zg < y:
                    gd,zg,r = x - y,y,i
    return r

#print(best_match([1, 2, 3, 4, 5],[0, 1, 2, 3, 4]))
