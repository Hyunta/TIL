import sys
n, m = map(int, input().split())
li = list([5000]*(n) for _ in range(n))

for _ in range(m):
    a,b,c = map(int, input().split())
    li[a-1][b-1] = c

for i in range(n):
    li[i][i]=0


for k in range(n):
    for i in range(n):
        for j in range(n):
            li[i][j] = min(li[i][j],li[i][k]+li[k][j])

for i in range(n):
    for j in range(n):
        if li[i][j] == 5000:
            print("M", end= ' ')
        else:
            print(li[i][j], end=' ')
    print()