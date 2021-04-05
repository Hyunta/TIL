'''
def solution(land):
    res=[]
    for z in range(4):
        tot = land[0][z]
        last = z
        for x in land[1:]:
            mx =0
            tmp = 4
            for i in range(4):
                if x[i] == mx:
                    tmp = 4
                if i != last and x[i] > mx:
                    mx = x[i]
                    tmp = i
            last = tmp
            tot += mx
        res.append(tot)
    return(max(res))
'''
def solution(land):
    dy = []
    for x in land[0]:
        dy.append(x)
    for y in land[1:]:
        tmp=dy.copy()
        for i in range(4):
            tmp[i] = y[i] + max(dy[:i] + dy[i+1:])
        dy = tmp
    print(max(dy))

solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]])