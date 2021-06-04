def DFS(v):
    if v > 15:
        return
    else:
        print(v, end=' ')
        DFS(v*2)
        DFS(v*2+1)
DFS(1)
