#최대점수 구하기(DFS)

def DFS(L,sum,t):
    global res
    if t > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1,sum+q[L][0],t+q[L][1])
        DFS(L+1,sum,t)



n,m = map(int, input().split())
q = list()
for _ in range(n):
    q.append(list(map(int, input().split())))
res = 0
DFS(0,0,0)
print(res)
