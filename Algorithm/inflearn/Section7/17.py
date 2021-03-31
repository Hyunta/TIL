import sys
def DFS(L,s):
    global res
    if L == m:
        sum = 0
        for i in hms:
            x1 = i[0]
            y1 = i[1]
            dis = 2147000000
            for x in cb:
                x2 = piz[x][0]
                y2 = piz[x][1]
                dis = min(dis,abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if sum < res:
            res = sum
    else:
        for i in range(s,len(piz)):
            cb[L]=i
            DFS(L+1,i+1)

if __name__ == "__main__":
    n,m = map(int, input().split())
    loc = [list(map(int, input().split())) for _ in range(n)]
    piz = []
    hms = []
    cb = [0]*m
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if loc[i][j] == 1:
                hms.append((i,j))
            elif loc[i][j] == 2:
                piz.append((i,j))
    DFS(0,0)
    print(res)
    