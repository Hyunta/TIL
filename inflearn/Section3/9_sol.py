n = int(input())
dx = [1,-1,0,0] 
dy = [0,0,1,-1]
M = [list(map(int, input().split())) for i in range(n)]
M.insert(0, [0]*n)
M.append([0]*n)
for m in M:
    m.insert(0,0)
    m.append(0)


cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        m = M[i][j]
        if all(m>M[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)