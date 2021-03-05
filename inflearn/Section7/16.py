
def DFS(x,y):
    ch[x][y]=1 
    if x == 0:
        print(y)
    else:
        if y-1>=0 and m[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x,y-1)
        elif y+1 <10 and m[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x,y+1)
        else:
            DFS(x-1,y)
           

if __name__ == "__main__":
    m = [list(map(int, input().split())) for _ in range(10)]
    li = [x for y in m for x in y]
    for k, v in enumerate(li):
        if v == 2:
            s = k//10
            e = k%10
    ch = [[0]*10 for _ in range(10) ]
    ch[s][e]=1
    DFS(s,e)
