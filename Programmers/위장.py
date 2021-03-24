def solution(clothes):
    d = dict()
    tot = 1
    for x in clothes:
        d[x[1]] = d.get(x[1],1)+1
    for x,y in d.items():
        tot *= y
    return tot-1