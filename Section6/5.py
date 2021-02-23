def DFS(L, sum):
    global res
    if sum > c:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1,sum+m[L])
        DFS(L+1,sum)    




if __name__ == "__main__":
    c,n = map(int, input().split())
    m = list(int(input()) for _ in range(n))
    res=0
    DFS(0,0)
    print(res)