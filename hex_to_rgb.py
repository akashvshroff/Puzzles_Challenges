def hex_string_to_RGB(hex_string):
    hex_string = hex_string[1:]
    sol = {}
    for i, c in zip(range(0, 6, 2), 'rgb'):
        val = int(hex_string[i], 16)*16 + int(hex_string[i+1], 16)
        sol[c] = val
    return sol


hex_string_to_RGB('#FFBB21')
print(int('0', 16))
