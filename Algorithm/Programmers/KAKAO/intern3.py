def solution(n, k, cmd):
    li = [m for m in range(n)]
    del_li = list()
    
    for c in cmd:
        if c[0] == "U":
            cnt = int(c[2:])
            k=li[li.index(k) - cnt]
        elif c[0] == "D":
            cnt = int(c[2:])
            k=li[li.index(k) + cnt]
        elif c[0] == "C":
            del_li.append(k)
            idx = li.index(k)
            li.remove(k)
            if k >= max(li):
                k = max(li)
            else:
                k = li[idx]
        elif c[0] == "Z":
            li.append(del_li.pop())
            li.sort()
            
    res =''
    for j in range(n):
        if j in del_li:
            res += 'X'
        else:
            res += 'O'
    return res