def num_record_breakers():
    """
    Find the number of record breaking days based on the following criteria:
    1. The attendance on that day has to be more than all the other days before
    it.
    2. If the day is not the last day, the attendance has to be more than the
    day after it.
    See also:
    https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08
    """
    num_cases = int(input())
    for test in range(num_cases):
        n = int(input())
        days = list(map(int, input().split()))
        mx = -1
        rec = 0
        for i in range(len(days)):
            if days[i] > mx:
                if i == len(days) - 1 or days[i] > days[i+1]:
                    rec += 1
                mx = days[i]
        print(f'Case #{test+1}: {rec}')


num_record_breakers()
