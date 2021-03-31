from collections import deque
s,e = map(int, input().split())
ch = [0] * 10000
d = [0] * 10000
ch[s] = 1
d[s] = 0
dQ = deque()
dQ.append(s)
while dQ:
    cur = dQ.popleft()
    if cur == e:
        break
    for com in (cur-1,cur+1,cur+5):
        if 0<com:
            if ch[com] == 0:
                dQ.append(com)
                ch[com]=1
                d[com]=d[cur]+1
print(d[e])
print(d)