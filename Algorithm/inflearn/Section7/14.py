from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
o = [x for y in m for x in y]
e = max(o)
s = min(o)
res = []

for i in range(s,e):
    ch = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if m[x][y] > i:
                ch[x][y] = 1
    cnt = 0
    
    for i2 in range(n):
        for j2 in range(n):
            if ch[i2][j2] == 1:
                ch[i2][j2] = 0
                Q=deque()
                Q.append((i2,j2))
                while Q:
                    tmp = Q.popleft()
                    for i3 in range(4):
                        x = tmp[0]+dx[i3]
                        y = tmp[1]+dy[i3]
                        if 0 <= x < n and 0<= y < n and ch[x][y] == 1:
                            ch[x][y] = 0
                            Q.append((x,y))
                cnt += 1
    res.append(cnt)
print(max(res))

