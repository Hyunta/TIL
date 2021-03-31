def DFS(w,v,last):
    if w > lim:
        res.append(v-last)
    else:
        for i in range(t):
            DFS(w+m[i][0],v+m[i][1],m[i][1])


if __name__ == "__main__":
    t, lim = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(t)]
    mx=0
    res = []
    DFS(0,0,0)
    print(max(res))