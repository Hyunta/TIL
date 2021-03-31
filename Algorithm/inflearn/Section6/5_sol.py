def DFS(L, sum, tsum):
    global res
    if sum+(total-tsum) < res:
        return
    if sum > c:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1,sum+m[L],tsum+m[L])
        DFS(L+1,sum,tsum+m[L])    




if __name__ == "__main__":
    c,n = map(int, input().split())
    m = list(int(input()) for _ in range(n))
    total = sum(m)
    res=0
    DFS(0,0,0)
    print(res)