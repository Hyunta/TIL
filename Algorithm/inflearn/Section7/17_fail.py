dx = [-1,0,1,0]
dy = [0,1,0,-1]

def DFS(x,y):
    global dis
    global ch
    if loc[x][y] == 2:
        tot.append(dis)
        ch =[[3]*n for _ in range(n)]
    else:
        for i in range(4):
            if 0<=x+dx[i]<n and 0<= y+dy[i]<n and ch[x+dx[i]][y+dy[i]] == 0:
                dis += 1
                print(dis)
                ch[x+dx[i]][y+dy[i]]=1
                DFS(x+dx[i],y+dy[i])
                dis -= 1
                print(dis)

if __name__ == "__main__":
    n,m = map(int, input().split())
    loc = [list(map(int, input().split())) for _ in range(n)]
    piz=[]
    hom=[]
    res=[]
    tot=[]
    z = [x for y in loc for x in y]
    for k, v in enumerate(z):
        if v == 2:
            piz.append((k//n,k%n))
        if v == 1:
            hom.append((k//n,k%n))
    for l in piz:
        tmp = 0
        for h in hom:
            tmp = tmp + abs(l[0]-h[0]) + abs(l[1]-h[1])
        res.append((l,tmp))
    close=sorted(res, key=lambda x:x[1])[m:]
    for x in close:
        loc[x[0][0]][x[0][1]]=0
    for h in hom:
        ch =[[0]*n for _ in range(n)]
        dis = 0
        print("h=",h)
        DFS(h[0],h[1])
    for x in loc:
        print(x)
    print()