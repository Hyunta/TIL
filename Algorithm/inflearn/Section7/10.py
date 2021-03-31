def DFS(x,y):
    global cnt
    if x == 6 and y ==6:
        cnt += 1
    else:
        for i in range(4):
            if 0 <= x+dx[i] < 7 and 0<= y+dy[i] < 7:
                if n[x+dx[i]][y+dy[i]] == 0 :
                    n[x][y]=1
                    DFS(x+dx[i],y+dy[i])
                    n[x][y]=0

if __name__ == "__main__":  
    n = [list(map(int, input().split())) for _ in range(7)]
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    cnt = 0
    n[0][0] = 1
    DFS(0,0)
    print(cnt)