from collections import deque
n,m = map(int, input().split())
tmp = map(int, input().split())

Q=deque()
for k,v in enumerate(tmp):
    Q.append([k,v])

cnt = 0
while True:
    x = Q.popleft()
    if any(x[1] < i[1] for i in Q):
        Q.append(x)
    else:
        cnt += 1
        if x[0] == m:
            print(cnt)
            break

