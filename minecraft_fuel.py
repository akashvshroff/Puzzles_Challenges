def calc_fuel(n):
    fuel_req = n*11
    f_r = fuel_req
    opt_available = {'lava':800,'blaze rod':120,'coal':80,'wood':15,'stick':1}
    final = {i:0 for i in opt_available.keys()}
    sm,name = 0,''
    num_items = 0
    for item,fuel in opt_available.items():
        if not fuel_req%fuel:
            if sm:
                if sm > fuel_req//fuel:
                    sm,name = fuel_req//fuel,item
            else:
                sm,name = fuel_req//fuel,item
        if fuel > f_r:
            continue
        final[item],f_r = divmod(f_r,fuel)
        num_items += final[item]
    if sm < num_items:
        final = {i:0 for i in opt_available.keys()}
        final[name] = sm
    return final
