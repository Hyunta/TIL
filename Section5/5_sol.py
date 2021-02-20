from collections import deque
n, k = map(int, input().split())
dq = list(range(1,n+1))
dq=deque(dq)

while len(dq)!=1:
    for _ in range(k-1):
        dq.append(dq.popleft())
    dq.popleft()
print(dq[0])