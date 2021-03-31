dx=[1,0,-1,0]
dy=[0,1,0,-1]
def DFS(x,y):
    global cnt
    m[x][y] = 0
    for i in range(4):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n:
            if m[x+dx[i]][y+dy[i]] == 1:
                cnt +=1
                DFS(x+dx[i],y+dy[i])
    
if __name__ == "__main__":
    n = int(input())
    m = [list(map(int,input())) for _ in range(n)]
    cnt = 1
    res = []
    for i in range(n):
        for j in range(n):
            if m[i][j]==1:
                DFS(i,j)
                res.append(cnt)
                cnt = 1
    print (len(res))
    for x in sorted(res):
        print(x)
        