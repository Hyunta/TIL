from collections import deque
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
sum = 0
Q = deque()
L=0
Q.append((n//2,n//2))

while True:
    if L == n//2:
        break
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0]+dx[j]
            y = tmp[1]+dy[j]
            if ch[x][y] == 0:
                sum += m[x][y]
                ch[x][y] = 1
                Q.append((x,y))
    L+=1
print(sum)
