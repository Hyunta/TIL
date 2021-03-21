def solution(priorities, location):
    q=[]
    cnt = 0
    for k,v in enumerate(priorities):
        q.append([k,v])
    while True:
        tmp = q.pop(0)
        if any(tmp[1]<x[1] for x in q):
            q.append(tmp)
        else:
            cnt += 1
            if tmp[0] == location:
                return cnt
                break