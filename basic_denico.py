def de_nico(key, msg):
    lk = len(key)
    order = [sorted(key).index(c) for c in key]
    res = ''
    while msg:
        res = res + ''.join(msg[i] for i in order if i < len(msg))
        msg =  msg[lk:]
    return res.rstrip()

#print(de_nico("crazy","cseerntiofarmit on"))
