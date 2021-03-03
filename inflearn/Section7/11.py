dx = [0,-1,0,1]
dy = [1,0,-1,0]

def DFS(x,y):
    global cnt
    if x == ex and y == ey:
        cnt+=1
    for i in range(4):
        if 0<= x+dx[i] < n and 0<= y+dy[i] < n:
            if m[x][y] < m[x+dx[i]][y+dy[i]]:
                DFS(x+dx[i],y+dy[i])

if __name__ == "__main__":
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    li = list(x for y in m for x in y)
    for k, v in enumerate(li):
        if v == max(li):
            ex = k//n
            ey = k % n
        if v == min(li):
            sx = k//n
            sy = k % n
    cnt = 0
    DFS(sx,sy)
    print(cnt)