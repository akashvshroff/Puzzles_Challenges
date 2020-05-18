def loose_change(coins_list, amount_of_change):
    l_ch = coins_list[::-1]
    amt = amount_of_change
    n, sm = 0, None
    for coin in l_ch:
        if amount_of_change % coin == 0:
            if sm:
                if amount_of_change/coin < sm:
                    sm = amount_of_change/coin
            else:
                sm = amount_of_change/coin
        if coin > amt:
            continue
        cs, amt = divmod(amt, coin)
        n += cs

    return n if sm > n else int(sm)


print(loose_change([1, 2, 4, 5, 10], 8))
