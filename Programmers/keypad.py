def solution(numbers, hand):
    ls = [1,4,7,'*']
    rs = [3,6,9,'#']
    lf = 10
    rf = 12
    a = ''
    for x in numbers:
        if x in ls:
            lf = x
            a += 'L'
        elif x in rs:
            rf = x
            a += 'R'
        else:
            x = 11 if x == 0 else x
            absL = abs(x-lf)
            absR = abs(x-rf)
            if sum(divmod(absL,3)) < sum(divmod(absR,3)):
                   lf = x
                   a += 'L'
            elif sum(divmod(absR,3))<sum(divmod(absL,3)):
                rf = x
                a += 'R'
            else:
                if hand == 'left':
                    lf = x
                    a += 'L'
                else:
                    rf = x
                    a += 'R'
    return a

    from itertools import combinations
    
    combinations(n,3)