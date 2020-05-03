from itertools import product
def get_pins(observed):
    combi = {'1':'124','2':'1235','3':'236', '4':'1457', '5':'24568', '6':'3569', '7':'478', '8':'58970', '9':'689','0':'08'}
    clist = [list(combi[l]) for l in observed]
    t = list(product(*clist))
    return [''.join(a) for a in t]
