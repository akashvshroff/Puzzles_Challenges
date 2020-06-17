def solution(args: list) -> str:
    '''
    Takes in a list of numbers and returns a string with all the ranges (more than 2)
    accounted for.
    >>> solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
    '-6,-3-1,3-5,7-11,14,15,17-20'
    '''
    start = args[0]
    curr_end = None
    res = ''
    i = 1
    for num in args[1:]:
        if start + i == num:
            i += 1
            curr_end = num
        else:
            if not curr_end:
                res += '{},'.format(start)
                start = num
            else:
                if curr_end - start == 1:
                    res += '{},{},'.format(start, curr_end)
                else:
                    res += '{}-{},'.format(start, curr_end)
                start, curr_end, i = num, None, 1
    if curr_end:  # to account for the last number
        if curr_end - start == 1:
            res += '{},{}'.format(start, curr_end)
        else:
            res += '{}-{}'.format(start, curr_end)
    else:
        res += '{}'.format(start)
    return res
