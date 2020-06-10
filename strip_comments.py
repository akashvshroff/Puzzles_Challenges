def solution(string, markers):
    res = ''
    mk_f = False
    lines = string.split('\n')
    for line in lines:
        mk_f = False
        for l in line:
            if l in markers:
                res += line[:line.index(l)].strip()
                mk_f = True
                break
        if not mk_f:
            res += line
        res += '\n'
    return res[:-1]


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
