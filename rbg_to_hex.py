def rgb(r, g, b):
    c_limit = lambda x: min(255, max(x, 0)) #input validation
    return ("{:02X}" * 3).format(c_limit(r), c_limit(g), c_limit(b))
