import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque()
for i in range(n):
    tmp = input().split()
    if tmp[0] == 'push':
        q.append(tmp[1])
    elif tmp[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif tmp[0] == 'size':
        print(len(q))
    elif tmp[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif tmp[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)