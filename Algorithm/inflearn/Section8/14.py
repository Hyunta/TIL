from collections import deque
n, m = map(int, input().split())
dis = list([0]*(n+1) for _ in range(n+1))
degree = [0]*(n+1)
for _ in range(m):
    a,b = map(int, input().split())
    dis[a][b] = 1
    degree[b] += 1
for x in dis:
    print(x)

dQ=deque()
for i in range(1,n+1):
    if degree[i] == 0:
        dQ.append(i)
while dQ:
    x=dQ.popleft()
    print(x, end=' ')
    for i in range(1, n+1):
        if dis[x][i] == 1:
            degree[i]-=1
            if degree[i]==0:
                dQ.append(i)
