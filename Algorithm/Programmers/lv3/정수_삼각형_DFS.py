def DFS(L,sum,t):
    global res
    if L == n:
        if sum > res:
            res = sum
    else:
        sum += triangle[L][t]
        DFS(L+1,sum,t)
        DFS(L+1,sum,t+1)

res = 0
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
n = len(triangle)
DFS(0,0,0)
print(res)
