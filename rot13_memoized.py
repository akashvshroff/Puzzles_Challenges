import string
def rot13(message):
    up = list(string.ascii_uppercase)
    lo = list(string.ascii_lowercase)
    s = ""
    cached = {}
    for l in message:
        if l in cached.keys():
            s+=cached[l]
            continue
        if not l.isalpha():
            s += l
        else:
            if l in up:
                i = up.index(l)
                if i > 12:
                    ni = i + 13 - 26
                else:
                    ni = i + 13
                cached[l] = up[ni]
                s += up[ni]
            elif l in lo:
                i = lo.index(l)
                if i > 12:
                    ni = i + 13 - 26
                else:
                    ni = i + 13
                cached[l] = lo[ni]
                s += lo[ni]

    return s
#print(rot13("Test"))
