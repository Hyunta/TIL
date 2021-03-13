n = int(input())
m = int(input())
dis = list([100001]*n for _ in range(n))

for i in range(n):
    dis[i][i] = 0
for _ in range(m):
    a,b,c = map(int, input().split())
    dis[a-1][b-1] = min(dis[a-1][b-1],c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])

for x in dis:
    for y in x:
        if y == 100001:
            print(0, end = ' ')
        else:
            print(y, end=' ')
    print()