n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

res=[]
for i in range(n):
    cnt = 0
    for j in range(n):
        if m[i][0]<m[j][0] and m[i][1]<m[j][1] and i != j:
            cnt += 1
    res.append(cnt+1)

for x in res:
    print(x, end=' ')
