from collections import deque
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dx = [-1,0,1,0,1,1,-1,-1]
dy = [0,1,0,-1,-1,1,-1,1]
Q=deque()

for i in range(n):
    for j in range(n):
        if m[i][j] == 1:
            m[i][j] = 0
            Q.append((i,j))
            while Q:
                tmp = Q.popleft()
                for p in range(8):
                    x = tmp[0]+dx[p]
                    y = tmp[1]+dy[p]
                    if 0<= x < n and 0<= y <n and m[x][y] == 1 :
                        m[x][y] = 0
                        Q.append((x,y))
            cnt += 1
print(cnt)