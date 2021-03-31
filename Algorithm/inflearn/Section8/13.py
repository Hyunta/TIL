n = int(input())
dis = list([100]*n for _ in range(n))

while True:
    x,y = map(int, input().split())
    if x == -1 and y == -1:
        break
    else:
        dis[x-1][y-1] = 1
        dis[y-1][x-1] = 1

for i in range(n):
    dis[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j] = min(dis[i][k]+dis[k][j], dis[i][j])
res = []
for x in dis:
    res.append(max(x))

print(min(res), res.count(min(res)))
for k,v in enumerate(res):
    if v == min(res):
        print(k+1, end=' ')

