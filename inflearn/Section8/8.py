def DFS(x,y):
    if dy[x][y] != 0:
        return dy[x][y]
    if (x,y) == (0,0):
        return m[x][y]
    else:
        if 0<x and 0<y:
            dy[x][y] = min(DFS(x-1,y),DFS(x,y-1))+m[x][y]
        elif x ==0 and y !=0:
            dy[x][y] = DFS(x,y-1)+m[x][y]
        elif y == 0 and x != 0:
            dy[x][y] = DFS(x-1,y)+m[x][y]
        return dy[x][y]

if __name__ == "__main__":
    n = int(input())
    m = [list(map(int,input().split())) for _ in range(n)]
    dy = list([0]*n for _ in range(n))
    print(DFS(n-1,n-1))
