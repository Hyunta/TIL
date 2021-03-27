'''
def solution(progresses, speeds):
    answer = []
    while sum(speeds) != 0:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
            if progresses[i] >= 100:
                cnt += 1
                progresses[i] = 0
                speeds[i] = 0
        if cnt != 0:
            answer.append(cnt)
    return answer
'''
def solution(progresses, speeds):
    p = progresses[::-1]
    s = speeds[::-1]
    res=[]
    while p:
        cnt = 0
        while p and p[-1] >= 100:
            p.pop()
            s.pop()
            cnt += 1
        if cnt != 0:
            res.append(cnt)
        for i in range(len(p)):
            if p[i] < 100:
                p[i] = p[i] + s[i]
    return res

solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])