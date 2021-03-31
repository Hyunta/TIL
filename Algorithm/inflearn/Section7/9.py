from collections import deque
n = [list(map(int, input().split())) for _ in range(7)]
ch = [[0]*7 for _ in range(7)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]
p = (0,0)
Q = deque()
Q.append(p)
L=0
ch[0][0]=1
while True:
    if L > 49:
        L=-1
        break
    if (6,6) in Q:
        break
    for x in range(len(Q)):
        tmp = Q.popleft()
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if 0 <= x < 7 and 0<= y < 7:
                if n[x][y]==0 and ch[x][y] == 0:
                    Q.append((x,y))
                    ch[x][y]=1
    L+=1
print(L)