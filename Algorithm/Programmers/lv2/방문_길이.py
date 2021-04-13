def solution(dirs):
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    d = {'U':0, 'D':1, 'R':2, 'L':3}

    v = set()
    x,y = 0,0
    cnt = 0
    for dir in dirs:
        i = d[dir]
        x2,y2 = x + dx[i],y + dy[i]
        if x2 < -5 or x2 > 5 or y2 < -5 or y2 > 5:
            continue
        if (x,y,x2,y2) not in v:
            v.add((x,y,x2,y2))
            v.add((x2,y2,x,y))
            cnt += 1
        x,y = x2,y2
    return cnt

print(solution("ULURRDLLU"))