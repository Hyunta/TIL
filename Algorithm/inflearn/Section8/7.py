n = int(input())
m = [list(map(int,input().split())) for _ in range(n)]
dy = list([0]*n for _ in range(n))
dy[0][0] = m[0][0]

for i in range(n):
    for j in range(n):
        if 0< i and 0 <j:
            dy[i][j] = min(dy[i-1][j], dy[i][j-1])+m[i][j]
        elif i == 0 and j != 0:
            dy[i][j] = dy[i][j-1]+m[i][j]
        elif j == 0 and i != 0:
            dy[i][j] = dy[i-1][j] + m[i][j]
print(dy[n-1][n-1])
