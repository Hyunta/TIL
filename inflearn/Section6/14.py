n,m = map(int, input().split())
li = [[0 for i in range(n)] for j in range(n)]

for _ in range(m):
    x = list(map(int,input().split()))
    li[x[0]-1][x[1]-1] = x[2]

for x in li:
    for j in x:
        print(j, end=' ')
    print()