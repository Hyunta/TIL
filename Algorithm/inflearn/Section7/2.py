def DFS(v,sum):
    global res
    if v > n:
        return
    if v == n:
        if sum > res:
            res = sum
    else:
        DFS(v+li[v][0],sum+li[v][1])
        DFS(v+1,sum)


if __name__ == "__main__":
    n = int(input())
    li = []
    for i in range(n):
        x,y = map(int, input().split())
        li.append((x,y))
    res = 0
    DFS(0,0)
    print(res)

