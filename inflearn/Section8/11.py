n,m = map(int, input().split())
li = [list(map(int,input().split())) for _ in range(n)]
li.insert(0,0)
dy = [[0] *(m+1) for _ in range(n+1)]


for i in range(1,n+1):
    tmp = dy[i-1]
    dy[i] = tmp
    for j in range(li[i][1],m+1):
        if dy[i-1][j-li[i][1]]+li[i][0] > dy[i][j]:
            dy[i][j] = dy[i-1][j-li[i][1]]+li[i][0]
print(dy[n][-1])